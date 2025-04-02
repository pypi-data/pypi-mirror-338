# Standard library imports
import os, warnings, platform, subprocess
from pathlib import Path
from time import time

# Third-party imports
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import hyperspy.api as hs
import skimage
import math
import scipy
import tifffile
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.widgets import RadioButtons, RangeSlider, Slider
from skimage.measure import label, regionprops_table, find_contours
from datetime import datetime
from copy import copy
from collections.abc import MutableSequence
from .utils import *

class NPSAMImage:
    """
    This class handles a single image and is meant as a base for the NPSAM class that
    handles more images, but NPSAMImage can also be used on its own.
    
    It loads the image upon initialization and offers methods for segmentation, 
    characterization and filtering of the resulting masks. It can also make an overview 
    .pdf file showing the segmentation and histograms of selected characteristics. 
    Finally, the segmented masks and characteristcs can be exported in different ways 
    (image files, numpy arrays and .csv files).
    """

    def __init__(self, filepath=None, select_image=None, segmentation_filepath=None):
        """
        Takes a given or prompted filepath and loads the file. Also loads any previous
        segmentation if saved to file.
        """
        if filepath is None:
            filepath = get_filepath()
        self.filepath = filepath
        self.load_image(filepath, select_image=select_image)
        self.seg = None
        self.cha = None
        try:
            self.load_segmentation(filepath=segmentation_filepath)
        except:
            pass


    def __repr__(self):
        """Returns the image name, masks segmented and how many passed the filtering."""
        # return f"NPSAMImage('{self.filepath}')"
        return self.__str__()


    def __str__(self):
        """Returns the image name, masks segmented and how many passed the filtering."""
        string = f"<NPSAM: {self.img.metadata.General.title}"
        if self.seg:
            string += f", {len(self.seg)} masks"
        if not self.cha is None:
            if not self.seg.metadata.has_item("Filtering.Conditions"):
                string += ", unfiltered"
            else:
                string += f", {self.cha['passed_filter'].sum()} passed filter"
        string += ">"
        return string


    def load_image(self, filepath, select_image=None):
        """
        This function loads either an image file (.png, .jpg, .tif, etc.) or an electron
        microscopy file (.emd, .bcf, .dm4, etc.). It returns the loaded image as a
        HyperSpy signal.
        """
        filepath = Path(filepath)

        # Hyperspy can't load all three channels in regular images, so we load them 
        # without
        if filepath.suffix in [".png", ".jpg", ".jpeg", ".gif"]:
            # Load image file as numpy array
            image_RGB = load_image_RGB(filepath)
            # Create hyperspy signal from image numpy array
            image = hs.signals.Signal1D(image_RGB)
        else:
            # Lazy loading doesn't seem to work with tif files
            if filepath.suffix in [".tif", ".tiff"]:
                lazy = False
            else:
                lazy = True
            
            if filepath.suffix in [".emd", ".bcf"]:
                # Apparently only works for .emd and .bcf. Throws error for .dm4
                signal = hs.load(filepath, lazy=lazy, select_type="images")
            else:
                signal = hs.load(filepath, lazy=lazy)

            # If there is more than one image in the file, we have to choose
            if isinstance(signal, list):

                # Check for empty list
                if len(signal) == 0:
                    print(f"No images found in {filepath}")
                    return

                # We take selection input until an image is found
                image_found = False
                while image_found == False:
                    if select_image is None:
                        print(f"Several signals are present in {filepath.name}:\n")
                        # Print name of the images in the file
                        for subsignal in signal:
                            print(str(subsignal))
                        select_image = input((
                            "\nPlease choose the image of interest by providing an "
                            "index or the image title:"
                        ))

                    try:
                        # If selection is an index
                        select_image = int(select_image)
                        image = signal[select_image]
                        image_found = True
                    except:
                        # If selection is not an index we check the title of the signal
                        for subsignal in signal:
                            if select_image == subsignal.metadata.General.title:
                                image = subsignal
                                image_found = True
                        if not image_found:
                            print("Image of interest not found.")
                            select_image = None
            else:
                image = signal
            if lazy:
                image.compute(show_progressbar=False)
            image = image.transpose()

        image.metadata.General.filepath = filepath.as_posix()
        image.metadata.General.title = filepath.name
        if not is_scaled(image):
            set_scaling(image, "1 px")
        self.img = image
        self.name = filepath.name


    def set_scaling(self, scaling, verbose=True):
        """
        Sets the scaling of the image. Scaling must be given as a Pint compatible
        quantity, e.g. '1 nm', '3.5 µm', '0.3 um' or '4 Å'.
        """
        set_scaling(self.img, scaling)
        try:
            set_scaling(self.seg, scaling)
            self._set_scaling_cha()
            if self.seg.metadata.has_item("Filtering.Conditions") and verbose:
                print("Scaling set, but area filtering conditions not updated.")
                print("Consider rerunning the filter function.")
        except:
            pass
            
    def _set_scaling_cha(self):
        length_per_pixel, unit = get_scaling(self.seg).split()
        length_per_pixel = float(length_per_pixel)
        self.cha["scaling [unit/px]"] = length_per_pixel
        self.cha["unit"] = unit

        for prop in [
            "equivalent_diameter_area",
            "feret_diameter_max",
            "perimeter",
            "perimeter_crofton",
        ]:
            self.cha[prop] = self.cha[prop+"_px"]*length_per_pixel
        for prop in ["area", "area_convex"]:
            self.cha[prop] = self.cha[prop+"_px"]*length_per_pixel**2

    def convert_to_units(self, units, verbose=True):
        """
        Converts the units of the image. units must be given as a Pint compatible
        unit, e.g. 'nm', 'µm', 'um' or 'Å'.
        """
        convert_to_units(self.img, units)
        try:
            convert_to_units(self.seg, units)
            self._set_scaling_cha()
            if self.seg.metadata.has_item("Filtering.Conditions") and verbose:
                print("Scaling set, but area filtering conditions not updated.")
                print("Consider rerunning the filter function.")
        except:
            pass

    def segment(
        self,
        device="auto",
        SAM_model="auto",
        PPS=64,
        shape_filter=True,
        edge_filter=True,
        crop_and_enlarge=False,
        invert=False,
        double=False,
        min_mask_region_area=100,
        stepsize=1,
        verbose=True,
        **kwargs,
    ):
        """
        This function segments the loaded image using either SAM or FastSAM. It saves 
        the masks in the .seg attribute as a HyperSpy signal and the segmentation 
        parameters stored in the .metadata attribute of this HyperSpy signal.

        Several parameters are available for the segmentation:
         - device: 'auto', 'cpu' or 'cuda'
         - SAM_model: 'auto', 'huge', 'large', 'base' or 'fast'
         - PPS (points per side) number of sampling points, default 64
         - shape_filter: True or False
         - edge_filter: True or False
         - crop_and_enlarge: True or False
         - invert: True or False
         - double: True or False
         - min_mask_region_area: 100 as default. Disconnected regions and holes in masks
           with area smaller than min_mask_region_area will be removed.
         - verbose: True or False
        """
        if device.lower() in ["auto", "a"]:
            device = choose_device()

        SAM_model = choose_SAM_model(SAM_model, device, verbose)

        image_shape = self.img.data.shape

        sub_images = preprocess(
            self.img, crop_and_enlarge=crop_and_enlarge, invert=invert, double=double
        )

        list_of_mask_arrays = []
        start = time()
        for sub_image in sub_images:
            if SAM_model == "fast":
                masks = FastSAM_segmentation(sub_image, device, min_mask_region_area)
            else:
                masks = SAM_segmentation(
                    sub_image, SAM_model, device, PPS, min_mask_region_area, **kwargs
                )
            
            masks = masks[masks.sum(axis=-1).sum(axis=-1)>0] # Remove empty masks
            
            for n,mask in enumerate(masks):
                labels = label(mask)
                if labels.max() > 1:
                    masks[n] = (labels == 1).astype('uint8')
                    for m in np.arange(1,labels.max())+1:
                        masks = np.concatenate((masks,np.expand_dims((labels == m).astype('uint8'),axis=0)))
                        
            masks = remove_overlapping_masks(masks)
            
            if edge_filter:
                edge_sums = masks[:, :, [0, 1, 2, -3, -2, -1]].sum(axis=1).sum(axis=1) + masks[
                    :, [0, 1, 2, -3, -2, -1], :
                ].sum(axis=2).sum(axis=1)
                # Only keep those where the edges are empty
                masks = masks[edge_sums == 0]
            
            if shape_filter:
                list_of_filtered_masks = []
                for mask in masks:
                    props = skimage.measure.regionprops_table(
                        label(mask), properties=["label", "area", "solidity"]
                    )
                    if len(props.get("label")) == 1 and (
                        props.get("area") < 400 or props.get("solidity") > 0.95
                    ):
                        list_of_filtered_masks.append(mask)
                masks = np.stack(list_of_filtered_masks)

            list_of_mask_arrays.append(masks)

        if crop_and_enlarge:
            stitched_masks = []
            for i in range(0, len(list_of_mask_arrays), 4):
                stitched_masks.append(
                    stitch_crops_together(list_of_mask_arrays[i : i + 4], image_shape)
                )
            list_of_mask_arrays = stitched_masks
        if double:
            masks = remove_overlapping_masks(np.concatenate(list_of_mask_arrays))
        else:
            masks = list_of_mask_arrays[0]

        if len(masks) == 0:
            elapsed_time = time() - start
            if verbose:
                print(
                    f"0 masks found for {self.name}, so no masks were saved."
                )
                print(f"It took {format_time(elapsed_time)}")
        else:
            segmentation_metadata = {
                "SAM_model": SAM_model,
                "PPS": PPS,
                "shape_filter": shape_filter,
                "edge_filter": edge_filter,
                "crop_and_enlarge": crop_and_enlarge,
                "invert": invert,
                "double": double,
                "min_mask_region_area": min_mask_region_area,
            }
            elapsed_time = time() - start
            if verbose:
                print(f"{len(masks)} masks found. It took {format_time(elapsed_time)}")

        self.seg = hs.signals.Signal2D(
            masks,
            metadata={
                "General": {
                    "title": self.img.metadata.General.title,
                    "image_filepath": self.filepath,
                },
                "Segmentation": segmentation_metadata,
                "Filtering": {},
            },
        )
        set_scaling(self.seg, get_scaling(self.img))

        self.characterize(stepsize=stepsize, verbose=verbose)

    def import_segmentation_from_image(self, filepath=None, stepsize=1, verbose=True):
        """
        Imports segmentation from an image file (black and white) instead of segmenting 
        with SAM. The segmentation is converted to a HyperSpy signal and saved in the
        .seg attribute.
        """
        if filepath is None:
            filepath = get_filepath()
        segmentation = load_image_RGB(filepath)
        if segmentation.ndim == 3:
            segmentation = segmentation[:, :, 0] > 0
        elif segmentation.ndim == 2:
            segmentation = segmentation > 0
        if segmentation.shape != self.img.data.shape[:2]:
            raise ValueError(f"The segmentation image dimensions {segmentation.shape} must match the original image dimensions {self.img.data.shape[:2]}.")
        labels = label(segmentation)
        masks = np.stack([labels == n for n in range(1, labels.max() + 1)]).astype(
            "uint8"
        )
        self.seg = hs.signals.Signal2D(
            masks,
            metadata={
                "General": {
                    "title": self.img.metadata.General.title,
                    "image_filepath": self.img.metadata.General.filepath,
                },
                "Filtering": {},
                "Segmentation": f"Imported from file '{filepath}'",
            },
        )
        set_scaling(self.seg, get_scaling(self.img))
        self.characterize(stepsize=stepsize, verbose=verbose)

    def combine(self, other_segmentation, iou_threshold=0.2, filtered=True):
        if isinstance(other_segmentation,str):
            selfcopy = copy(self)
            selfcopy.import_segmentation_from_image(other_segmentation,verbose=False)
            other_segmentation = selfcopy
        
        if filtered:
            own_masks = self.seg.data[self.cha["passed_filter"]]
            other_masks = other_segmentation.seg.data[other_segmentation.cha["passed_filter"]]
        else:
            own_masks = self.seg.data
            other_masks = other_segmentation.seg.data
        
        edge_sums = other_masks[:, :, [0, 1, -2, -1]].sum(axis=1).sum(axis=1) + other_masks[
                    :, [0, 1, -2, -1], :
                ].sum(axis=2).sum(axis=1)
        # Only keep those where the edges are empty
        other_masks = other_masks[edge_sums == 0]
        
        own_segmentation = seg_params_to_str(self.seg.metadata.Segmentation)
        other_segmentation = seg_params_to_str(other_segmentation.seg.metadata.Segmentation)
        segmentations = [own_segmentation]*len(own_masks)+[other_segmentation]*len(other_masks)
        
        all_masks = np.concatenate([own_masks,other_masks])
        
        processed_masks, indices = remove_overlapping_masks(all_masks,iou_threshold=iou_threshold,return_indices=True)
        kept_segmentations = [segmentations[i] for i in indices]
        
        self.seg.data = processed_masks
        self.characterize()
        self.cha["segmentation"] = kept_segmentations
        self.seg.metadata.Segmentation = "Combined segmentation"
        
    def characterize(self, stepsize=1, verbose=True):
        """
        Calculates a range of characteristics for each mask and saves it as a Pandas
        DataFrame in the .cha attribute.
        
        Also finds mask contours and saves them in .seg.metadata.Filtering.contours.
        """
        masks = self.seg.data
        dfs_properties = []
        for m, mask in enumerate(masks):
            if verbose:
                print(
                    f"Finding mask characteristics: {m + 1}/{len(masks)}",
                    sep=",",
                    end="\r" if m + 1 < len(masks) else "\n",
                    flush=True,
                )
            if self.img.data.ndim == 3:
                img = self.img.data.mean(axis=2)
            else:
                img = self.img.data
            dfs_properties.append(
                pd.DataFrame(
                    regionprops_table(
                        mask,
                        img,
                        properties=(
                            "area",
                            "area_convex",
                            "axis_major_length",
                            "axis_minor_length",
                            "bbox",
                            "centroid",
                            "centroid_local",
                            "centroid_weighted",
                            "eccentricity",
                            "equivalent_diameter_area",
                            "euler_number",
                            "extent",
                            "feret_diameter_max",
                            "inertia_tensor",
                            "inertia_tensor_eigvals",
                            "intensity_max",
                            "intensity_mean",
                            "intensity_min",
                            "moments_hu",
                            "moments_weighted_hu",
                            "orientation",
                            "perimeter",
                            "perimeter_crofton",
                            "solidity",
                        ),
                    )
                )
            )
        df = pd.concat(dfs_properties)
        length_per_pixel = float(get_scaling(self.seg).split()[0])
        unit = get_scaling(self.seg).split()[1]
        df["scaling [unit/px]"] = length_per_pixel
        df["unit"] = unit
        df["mask"] = np.arange(df.shape[0])
        df["mask_index"] = np.arange(df.shape[0])
        column_to_move = df.pop("mask_index")
        df.insert(0, "mask_index", column_to_move)
        df = df.set_index("mask")

        for prop in [
            "equivalent_diameter_area",
            "feret_diameter_max",
            "perimeter",
            "perimeter_crofton",
        ]:
            df[prop+"_px"] = df[prop]
            df[prop] *= length_per_pixel
        for prop in ["area", "area_convex"]:
            df[prop+"_px"] = df[prop].astype(int)
            df[prop] *= length_per_pixel**2

        flattened_multiple_masks = np.moveaxis(masks[:, masks.sum(axis=0) > 1], 0, -1)
        unique_multiple_masks = nb_unique_caller(flattened_multiple_masks[::stepsize])
        df["overlap"] = 0
        df["overlapping_masks"] = [set() for _ in range(len(df))]

        overlap_counts = np.zeros(len(df), dtype=int)

        if not (unique_multiple_masks is None):
            for n, unique in enumerate(unique_multiple_masks):
                if verbose:
                    print((
                            "Finding areas with overlap: "
                            f"{n + 1}/{len(unique_multiple_masks)}"
                        ),
                        sep=",",
                        end="\r" if n + 1 < len(unique_multiple_masks) else "\n",
                        flush=True,
                    )
                    

                mask_indices = np.where(unique)[0]

                for idx in mask_indices:
                    df.at[idx, "overlapping_masks"].update(mask_indices)
                    df.at[idx, "overlapping_masks"].remove(idx)

                summed_masks = masks[mask_indices].sum(axis=0)
                overlaps = (summed_masks > 1).sum(axis=(0, 1))

                overlap_counts[mask_indices] += overlaps

        df["overlap"] = overlap_counts
        df["number_of_overlapping_masks"] = df["overlapping_masks"].apply(len)

        df["number_of_overlapping_masks"] = [
            len(masks) for masks in df["overlapping_masks"].to_list()
        ]
        df["passed_filter"] = True
        df.attrs = {
            "title": self.img.metadata.General.title,
            "image_filepath": self.filepath,
            "filepath": "Not saved yet",
        }
        self.cha = df
        for n,mask in enumerate(self.seg.data):
            self.seg.metadata.set_item(
                f"Filtering.Contours.{n}", 
                find_contours(mask, 0.5)[0]
            )

    def save_segmentation(self, save_as=None, overwrite=None):
        """
        Saves the segmentation as a .hspy file and the characterization as a .csv file
        for loading later. Filtering conditions are also saved in the .hspy file.
        """
        if save_as is None:
            filepath = Path(self.filepath).parent / ("NP-SAM_results/"+Path(self.filepath).name)
        else:
            filepath = Path(save_as)
        #filepath = Path(self.filepath if save_as is None else save_as)
        self.seg.save(filepath.with_suffix(".hspy"), overwrite=overwrite)
        save_df_to_csv(self.cha, filepath.with_suffix(".csv"))

    def load_segmentation(self, filepath=None):
        """
        Loads segmentation, characterization and filtering from a .hspy and .csv file.
        """
        if filepath is None:
            filepath = Path(self.filepath).parent / ("NP-SAM_results/"+Path(self.filepath).name)
        else:
            filepath = Path(filepath)
        #filepath = Path(self.filepath if filepath is None else filepath)
        self.seg = hs.load(filepath.with_suffix(".hspy"))
        self.cha = load_df_from_csv(filepath.with_suffix(".csv"))
        

    def plot_masks(self, cmap="default", alpha=0.3, figsize=[8, 4],filtered=False, legacy=False):
        """
        Plots the original image and the masks found through segmentation. If
        filtered is True, it only plots the masks that passed the filtering 
        conditions.
        """
        fig, axs = plt.subplots(1, 2, figsize=figsize)
        
        for ax in axs:
            ax.imshow(self.img.data, cmap="gray")
            ax.axis("off")

        cs = plot_masks(self, ax=axs[1], alpha=alpha, cmap=cmap, filtered=filtered)
        
        plt.suptitle(self.img.metadata.General.title)
        plt.tight_layout()
        plt.show()

    def plot_particle(self, mask_index, cmap="grey"):
        """
        Given a particle/mask index, it plots the smallest image that contains the given
        mask. It plots both filtered and non-filtered masks.
        """
        try:
            bbox = self.cha.loc[mask_index, [f"bbox-{n}" for n in range(4)]].tolist()
        except:
            raise ValueError(f"Only indices between 0 and {self.cha['mask_index'].max()} are accepted.")
        fig, ax = plt.subplots()
        ax.imshow(self.img.data[bbox[0] : bbox[2], bbox[1] : bbox[3]], cmap=cmap)
        plt.show()

    def filter(self, cmap="default", alpha=0.3):
        """
        Runs the interactive filtering window to filter masks based on selected
        characteristcs.
        """
        filter(self, cmap=cmap, alpha=alpha)

    def filter_nogui(self, conditions):
        """
        Filters the masks based on a set of conditions with respect to the mask
        characteristics. No interactive window opens. Conditions are passed as a 
        dictionary with the following possible keys:
        
        - max_area
        - min_area
        - max_intensity
        - min_intensity
        - max_eccentricity
        - min_eccentricity
        - max_solidity
        - min_solidity
        - overlap
        - overlapping_masks
        """
        filter_nogui(self, conditions)
        
    def overview(
        self, 
        save_as=None,
        characteristics=["area"], 
        bin_list=None, 
        timestamp=False
    ):
        """
        Produces and saves an overview .pdf file showing the segmentation and histograms
        of selected characteristics.
        """
        if characteristics == ["all"]:
            characteristics = [
                "area",
                "area_convex",
                "axis_major_length",
                "axis_minor_length",
                "eccentricity",
                "equivalent_diameter_area",
                "extent",
                "feret_diameter_max",
                "intensity_max",
                "intensity_mean",
                "intensity_min",
                "orientation",
                "perimeter",
                "perimeter_crofton",
                "solidity",
                "overlap",
            ]

        for n, prop in enumerate(characteristics):
            if prop == "intensity":
                characteristics[n] = "intensity_mean"
            elif prop == "diameter":
                characteristics[n] = "equivalent_diameter_area"
            elif prop == "max diameter":
                characteristics[n] = "feret_diameter_max"
            elif prop == "crofton perimeter":
                characteristics[n] = "perimeter_crofton"
            elif prop == "convex area":
                characteristics[n] = "area_convex"

        df = copy(self.cha[self.cha["passed_filter"]])

        if bin_list is None:
            bin_list = ["auto"] * len(characteristics)

        unit = df["unit"].to_list()[0]
        unit2 = unit + "$^2$" if unit != "px" else unit
        name_dict = {
            "area": f"area ({unit2})",
            "area_convex": f"convex area ({unit2})",
            "eccentricity": "eccentricity",
            "solidity": "solidity",
            "intensity_mean": "mean intensity",
            "overlap": "overlap (px)",
            "equivalent_diameter_area": f"area equivalent diameter ({unit})",
            "feret_diameter_max": f"Max diameter (Feret) ({unit})",
            "orientation": "orientation",
            "perimeter": f"perimeter ({unit})",
            "perimeter_crofton": f"crofton perimeter ({unit})",
            "axis_major_length": f"Major axis length ({unit})",
            "axis_minor_length": f"Minor axis length ({unit})",
            "extent": "Ratio of pixels in the mask the pixels in the bounding box",
            "intensity_max": "Max intensity of the mask",
            "intensity_min": "minimum intensity of the mask",
            "overlap": f"amount of overlap ({unit2})",
        }
        figs = []
        for n, prop in enumerate(characteristics):
            fig, ax = plt.subplots(figsize=(11.7, 8.3))
            ax.set_xlabel(name_dict.get(prop).capitalize(), fontsize=16)
            ax.set_title(f"Histogram of {name_dict.get(prop)} for all images", fontsize=18)
            df[prop].hist(bins=bin_list[n], ax=ax, edgecolor="k", color="#0081C6")
            ax.grid(False)
            ax.set_ylabel("Count", fontsize=16)
            ax.tick_params(axis="both", which="major", labelsize=14)
            data = df[prop]
            mean = np.mean(data)
            median = np.median(data)
            std_dev = np.std(data)
            variance = np.var(data)
            skewness = scipy.stats.skew(data)
            kurtosis = scipy.stats.kurtosis(data)
            data_range = np.ptp(data)
            q1 = np.percentile(data, 25)
            q3 = np.percentile(data, 75)
            iqr = scipy.stats.iqr(data)
            minimum = np.min(data)
            maximum = np.max(data)
            count = len(data)
            total_sum = np.sum(data)
            coeff_variation = std_dev / mean

            def format_value(val):
                if val == 0:
                    return 0
                elif val < 10:
                    return f"{val:.2f}"
                elif 10 <= val < 100:
                    return f"{val:.1f}"
                elif 100 <= val:
                    return f"{int(val)}"

            x_r = 1 - len(f"Upper quantile: {format_value(q3)}") * 0.0108
            x_m = (
                x_r - 0.025 - len(f"Sum: {format_value(total_sum)}") * 0.0108
                if total_sum > 100000000
                else x_r - 0.155
            )
            x_l = (
                x_m - 0.055 - len(f"Sum: {format_value(variance)}") * 0.0108
                if variance > 1000000000000
                else x_m - 0.22
            )

            stats_text_left = (
                f"Mean: {format_value(mean)}\nStd Dev: {format_value(std_dev)}\n"
                f"Median: {format_value(median)}\nVariance: {format_value(variance)}\n"
                f"Coeff of Variation: {format_value(coeff_variation)}\n"
                f"Total number of masks: {len(df['area'].to_list())}"
            )

            stats_text_middle = (
                f"Skewness: {format_value(skewness)}\nKurtosis: {format_value(kurtosis)}\n"
                f"Count: {count}\nSum: {format_value(total_sum)}\nIQR: {format_value(iqr)}"
            )

            stats_text_right = (
                f"Lower quantile: {format_value(q1)}\nUpper quantile: {format_value(q3)}\n"
                f"Min: {format_value(minimum)}\nMax: {format_value(maximum)}\n"
                f"Range: {format_value(data_range)}"
            )
            n = "i" * int((194 * (1 - x_l + 0.011)))

            text = f"{n}\n{n}\n{n}\n{n}\n{n}\n{n}"
            text_properties = {
                "fontsize": 12,
                "color": "none",
                "verticalalignment": "top",
                "bbox": dict(
                    boxstyle="round,pad=0.3",
                    edgecolor="black",
                    facecolor="white",
                    alpha=0.5,
                ),
            }

            plt.text(x_l, 0.98, text, transform=plt.gca().transAxes, **text_properties)
            for x, txt in zip([x_l,x_m,x_r],[stats_text_left,stats_text_middle,stats_text_right]):
                plt.text(
                    x, 0.98,
                    txt,
                    ha="left",
                    va="top",
                    transform=plt.gca().transAxes,
                    fontsize=12,
                )
            
            figs.append(fig)

        figs.append(self._make_overview_figure())

        if timestamp:
            d = datetime.now()
            stamp = f"_{d.year}{d.month}{d.day}_{d.hour}{d.minute}{d.second}"
        else:
            stamp = ""

        filepath = self._save_as_to_filepath(save_as, end=f"_overview{stamp}.pdf")
        
        p = PdfPages(filepath)

        for fig in figs:
            fig.savefig(p, format="pdf")

        p.close()
        plt.show()
        
    def _make_overview_figure(self,cmap="default",alpha=0.3):
        df = self.cha[self.cha["passed_filter"]]
        
        fig, ax = plt.subplot_mosaic(
            [["left", "right"], ["left2", "right2"]],
            constrained_layout=True,
            figsize=(11.7, 8.3),
        )
        ax["left"].imshow(self.img.data, cmap="gray")
        ax["left"].axis("off")

        ax["right"].imshow(self.img.data, cmap="gray")
        ax["right"].axis("off")
        cs = plot_masks(self, ax=ax["right"], cmap=cmap, alpha=alpha)
        for n, visibility in enumerate(self.cha["passed_filter"]):
            cs[n].set_visible(visibility)

        ax["right2"].axis("off")

        plt.suptitle(self.seg.metadata.General.title, fontsize=18)

        df["area"].hist(
            bins="auto", ax=ax["left2"], edgecolor="k", color="#0081C6"
        )
        unit = df["unit"].to_list()[0]
        unit2 = unit + "$^2$" if unit != "px" else unit
        ax["left2"].set_title(f"Histogram of area ({unit})")
        ax["left2"].set_xlabel(f"area ({unit})")
        ax["left2"].grid(False)
        ax["left2"].set_ylabel("Count")

        try:
            filters = self.seg.metadata.Filtering.Conditions.as_dictionary()
        except:
            self.filter_nogui({"min_area":0})
            filters = self.seg.metadata.Filtering.Conditions.as_dictionary()
        min_area, max_area = filters["area"]
        min_solidity, max_solidity = filters["solidity"]
        min_intensity, max_intensity = filters["intensity_mean"]
        min_eccentricity, max_eccentricity = filters["eccentricity"]
        min_overlap, max_overlap = filters["overlap"]
        overlapping_masks = filters["number_of_overlapping_masks"]
        scaling, unit = get_scaling(self.seg).split()
        scaling = float(scaling)
        removed = (~self.cha["passed_filter"]).sum()
        remain = self.cha["passed_filter"].sum()
        segmentation = seg_params_to_str(self.seg.metadata.Segmentation)

        x1 = 0.5845
        x2 = 0.8
        fig.text(x1, 0.495, "Used parameter values:", fontsize=18)

        fig.text(x1, 0.455, "Segmentation:", fontsize=18)
        fig.text(0.75, 0.455, segmentation, fontsize=18)

        fig.text(x1, 0.415, f"Area ({unit2}):", fontsize=18)
        fig.text(
            x2, 0.415, f"({min_area:.5g}, {max_area:.5g})", fontsize=18
        )

        fig.text(x1, 0.375, "Solidity:", fontsize=18)
        fig.text(x2, 0.375, f"({min_solidity:.5g}, {max_solidity:.5g})", fontsize=18)

        fig.text(x1, 0.335, "Intensity:", fontsize=18)
        fig.text(x2, 0.335, f"({min_intensity:.5g}, {max_intensity:.5g})", fontsize=18)

        fig.text(x1, 0.295, "Eccentricity:", fontsize=18)
        fig.text(x2, 0.295, f"({min_eccentricity:.5g}, {max_eccentricity:.5g})", fontsize=18)

        fig.text(x1, 0.255, "Overlap:", fontsize=18)
        fig.text(x2, 0.255, f"({min_overlap:.5g}, {max_overlap:.5g})", fontsize=18)

        fig.text(x1, 0.185, "Number of \noverlapping masks:", fontsize=18)
        fig.text(x2, 0.185, f"{overlapping_masks}", fontsize=18)

        fig.text(x1, 0.145, f"Scaling (px/{unit}):", fontsize=18)
        fig.text(x2, 0.145, f"{scaling:.5g}", fontsize=18)
        fig.text(
            0.63,
            0.055,
            f"{removed} masks removed.\n {remain} remain.",
            fontsize=18,
            multialignment="center",
        )
        
        return fig
        

    def get_filtered_masks(self):
        """
        Returns the masks that passed the filtering conditions.
        """
        return self.seg.data[self.cha["passed_filter"]]

    def export_filtered_characteristics(self, save_as=None):
        """
        Exports the characteristics of the masks that passed the filtering conditions as
        a .csv file.
        """
        filtered_characteristic = self.cha[self.cha["passed_filter"] == True]
        filtered_characteristic.loc[:, "mask_index"] = np.arange(
            len(filtered_characteristic)
        )
        filepath = self._save_as_to_filepath(save_as, end="_filtered_masks.csv")
        save_df_to_csv(filtered_characteristic, filepath.with_suffix(".csv"))

    def export_filtered_masks_png(self, save_as=None, cmap="default",alpha=0.3):
        """
        Exports an image of the masks that passed the filtering conditions as a .png
        file.
        """
        plt.ioff()
        imy, imx = self.img.data.shape[:2]
        fig, ax = plt.subplots(figsize=[imx/100,imy/100])
        ax.set_position([0,0,1,1])
        ax.axis("off")
        ax.imshow(self.img.data, cmap="gray")
        cs = plot_masks(self,ax=ax,cmap=cmap,alpha=alpha)
        for n, visibility in enumerate(self.cha["passed_filter"]):
            cs[n].set_visible(visibility)
        filepath = self._save_as_to_filepath(save_as, end="_filtered_masks.png")
        fig.savefig(filepath.with_suffix(".png"),dpi=100)
        plt.close(fig)
        plt.ion()

    def export_filtered_masks_tif(self, save_as=None):
        """
        Exports an image of the masks that passed the filtering conditions as a .tif
        file.
        """
        labels = masks_to_2D(self.get_filtered_masks())
        filepath = self._save_as_to_filepath(save_as, end="_filtered_masks.tif")
        tifffile.imwrite(filepath.with_suffix(".tif"), labels.astype("uint16"))

    def export_filtered_masks_binary(self, save_as=None):
        """
        Exports an image of the masks that passed the filtering conditions as a binary 
        .tif file.
        """
        labels = masks_to_2D(self.get_filtered_masks())
        filepath = self._save_as_to_filepath(save_as, end="_filtered_masks_binary.tif")
        tifffile.imwrite(
            filepath.with_suffix(".tif"), ((labels > 0) * 255).astype("uint8")
        )

    def export_filtered_masks_numpy(self, save_as=None):
        """
        Exports the masks that passed the filtering conditions as a compressed .npz
        file. Can be loaded again with:
        
        import numpy as np
        masks = np.load('filename.npz')['array']
        """
        filepath = self._save_as_to_filepath(save_as, end="_filtered_masks_binary.npz")
        np.savez_compressed(
            filepath.with_suffix(".npz"), array=self.get_filtered_masks()
        )

    def export_all(self, save_as=None):
        """
        Exports all the different outputs possible.
        """
        self.export_filtered_characteristics(save_as=save_as)
        self.export_filtered_masks_png(save_as=save_as, cmap="default")
        self.export_filtered_masks_tif(save_as=save_as)
        self.export_filtered_masks_binary(save_as=save_as+"_binary" if save_as else save_as)
        self.export_filtered_masks_numpy(save_as=save_as)
        
        
    def _save_as_to_filepath(self, save_as, end=None):
        """
        Helper function. Chooses a default filename or the given save_as and returns it 
        as a Path object.
        """
        if save_as is None:
            filepath = Path(self.filepath).parent / ("NP-SAM_results/"+Path(self.filepath).name.split(".")[0] + end)
            filepath.parent.mkdir(exist_ok=True)
        else:
            filepath = Path(save_as)
        
        #if save_as is None:
        #    filepath = Path(self.filepath.split(".")[0] + end)
        #else:
        #    filepath = Path(save_as)
        return filepath


class NPSAM(MutableSequence):
    """
    This class is a wrapper around the NPSAMImage class that enables segmentation of
    multiple images with NP-SAM.
    
    Upon initialization, it loads images from filepaths given as input. If no filepaths
    are given, the user is prompted to select files.

    The loaded images can then be segmented with the .segment() function, and the masks 
    stored in the .seg attribute. The masks are then characterized and the 
    characteristics are stored as pandas DataFrames in the .cha attribute. If no scaling 
    is given or extracted from the image files, the user is prompted for a scaling. The 
    scaling can also be changed with .set_scaling() at any time.

    Once segmented, the masks can be filtered with .filter() or .filter_nogui(). Only
    masks that passed the filtering conditions will have True in their 'passed_filter' 
    characteristic.

    Finally, a range of different outputs can be made. An overview .pdf file with
    .overview(), a .csv file with the characteristics of the filtered masks, an .npz
    file with a numpy array of the filtered masks and .png or .tif images of the 
    filtered masks.
    """

    def __init__(self, images=None, select_image=None, select_files="*"):
        if images is None:
            images = get_filepaths()
        else:
            if isinstance(images,str):
                images = Path(images)
            if isinstance(images,Path):
                if images.is_dir():
                    images = [f for f in images.glob(select_files) if (
                        f.is_file() 
                        and not ".DS_Store" in f.as_posix()
                        and not "desktop.ini" in f.as_posix()
                    )]
                elif images.is_file():
                    images = [images]
                else:
                    raise ValueError(f"images='{images}' is neither a file nor a directory.")
            if isinstance(images,NPSAMImage):
                images = [images]
        self.data = [
            self._validatetype(image, select_image=select_image) for image in images
        ]
        self._update()


    def __repr__(self):
        return repr(self.data).replace(">, <", ">,\n <")
      
      
    def __str__(self):
        return str(self.data).replace(">, <", ">,\n <")


    def __len__(self):
        return len(self.data)


    def __getitem__(self, i):
        if isinstance(i, int):
            return self.data[i]
        else:
            return self.__class__(self.data[i])


    def __setitem__(self, i, image):
        self.data[i] = self._validatetype(image)
        self._update()


    def __delitem__(self, i):
        del self.data[i]
        self._update()


    def __add__(self, other):
        if isinstance(other, NPSAM):
            return self.__class__(self.data + other.data)
        elif isinstance(other, NPSAMImage):
            return self.__class__(self.data + [other])
        else:
            raise TypeError("Can only add NPSAM objects")


    def insert(self, i, image):
        self.data.insert(i, self._validatetype(image))
        self._update()


    def _validatetype(self, item, select_image=None):
        if isinstance(item, NPSAMImage):
            return item
        if isinstance(item, Path):
            if item.is_file():
                return NPSAMImage(item.as_posix(), select_image=select_image)
        if isinstance(item, str):
            return NPSAMImage(item, select_image=select_image)
        raise TypeError("Only NPSAMImage objects or filepaths are supported")


    def _update(self):
        self.img = [image.img for image in self.data]
        self.seg = [image.seg for image in self.data]
        self.cha = [image.cha for image in self.data]
        self.filepaths = [image.filepath for image in self.data]

    def set_scaling(self, scaling = True):
        """
        Sets the scaling of the images. Scaling must be given as a (list of) Pint 
        compatible quantity, e.g. '1 nm', '3.5 µm', '0.3 um' or '4 Å'. If none are
        given, the user is prompted.
        """
        if scaling is True:
            common_scaling = input("Do you want to use the same scaling for all images? (Y/n) ")
            if common_scaling.lower() in ["y","yes",""]:
                scalings = input("What is the scaling? (E.g. '2.5 nm') ")
                scalings = len(self)*[scalings]
            else:
                scalings = []
                for image in self:
                    scalings.append(input(f"What is the scaling for {image.img.metadata.General.title}? (E.g. '2.5 nm') "))
        elif scaling is False:
            scalings = len(self)*["1 px"]
        elif isinstance(scaling, str):
            scalings = len(self)*[scaling]
        elif isinstance(scaling, list):
            scalings = scaling
        else:
            raise ValueError("scaling must be given as a string or a list of strings.")
            
        if len(self) == len(scalings):
            printed_yet = False
            for image, scaling in zip(self, scalings):
                image.set_scaling(scaling,verbose=not printed_yet)
                try:
                    if not image.seg.metadata.Filtering.Conditions is None:
                        printed_yet = True
                except:
                    pass
        else:
            raise ValueError(f"The number of scalings ({len(scalings)}) does not correspond to the number of images ({len(self)}).")
       

    def convert_to_units(self, units=None):
        """
        Converts the units of the image. units must be given as a (list of) Pint 
        compatible unit, e.g. 'nm', 'µm', 'um' or 'Å'. If none are given, the user is 
        prompted.
        """
        if units is None:
            common_units = input("Do you want to convert to the same units for all images? (Y/n) ")
            if common_units.lower() in ["y","yes",""]:
                units = input("What is the units? (E.g. 'nm') ")
                units = len(self)*[units]
            else:
                units = []
                for image in self:
                    units.append(input(f"What is the units for {image.img.metadata.General.title}? (E.g. 'nm') "))
        elif isinstance(units, str):
            units = len(self)*[units]
        elif isinstance(units, list):
            pass
        else:
            raise ValueError("units must be given as a string or a list of strings.")
            
        if len(self) == len(units):
            printed_yet = False
            for image, unit in zip(self, units):
                image.convert_to_units(unit,verbose=not printed_yet)
                try:
                    if not image.seg.metadata.Filtering.Conditions is None:
                        printed_yet = True
                except:
                    pass
        else:
            raise ValueError(f"The number of units ({len(units)}) does not correspond to the number of images ({len(self)}).")


    def segment(
        self,
        device="auto",
        SAM_model="auto",
        PPS=64,
        shape_filter=True,
        edge_filter=True,
        crop_and_enlarge=False,
        invert=False,
        double=False,
        min_mask_region_area=100,
        stepsize=1,
        verbose=True,
        **kwargs,
    ):
        if device.lower() in ["auto", "a"]:
            device = choose_device()

        SAM_model = choose_SAM_model(SAM_model, device, verbose)

        for n, image in enumerate(self):
            if len(self) > 1:
                print(
                    f"{n + 1}/{len(self)} - Now working on: {image.name}"
                )

            image.segment(
                device=device,
                SAM_model=SAM_model,
                PPS=PPS,
                shape_filter=shape_filter,
                edge_filter=edge_filter,
                crop_and_enlarge=crop_and_enlarge,
                invert=invert,
                double=double,
                min_mask_region_area=min_mask_region_area,
                stepsize=stepsize,
                verbose=verbose,
                **kwargs,
            )

            if len(self) > 1:
                print("")

            self._update()
            
    def characterize(self, stepsize=1, verbose=True):
        for im in self:
            im.characterize(stepsize=stepsize, verbose=verbose)


    def save_segmentation(self, save_as = None, overwrite = None):
        """
        Saves segmentation, characterization and filtering to a subfolder with the
        save_as argument as the name of the subfolder. If None is given, the folder
        will be called NP-SAM_results.
        """
        for image in self:
            if not save_as is None:
                filepath = Path(image.filepath).parent / (f"{save_as}/"+Path(image.filepath).name)
                filepath.parent.mkdir(exist_ok=True)
                _save_as = filepath.as_posix()
            else:
                _save_as = save_as
            image.save_segmentation(overwrite = overwrite, save_as=_save_as)
    
    
    def load_segmentation(self, foldername=None):
        """
        Loads segmentation, characterization and filtering from .hspy and 
        .csv files in a folder given by the foldername argument. If None, it looks for
        a folder callen NP-SAM_results.
        """
        for image in self:
            if not foldername is None:
                filepath = (Path(image.filepath).parent / (f"{foldername}/"+Path(image.filepath).name)).as_posix()
            else:
                filepath = None
            image.load_segmentation(filepath=filepath)
        self._update()
            
    
    def plot_masks(self, cmap="default", alpha=0.3, figsize=[8, 4], filtered=False):
        for image in self:
            image.plot_masks(cmap=cmap, alpha=alpha, figsize=figsize, filtered=filtered)
            
    
    def plot_particle(self, image_index, mask_index, cmap="grey"):
        self[image_index].plot_particle(mask_index,cmap=cmap)
    

    def filter(self, cmap="default", alpha=0.3, app=False, position=None):
        self._update()
        filter(self, cmap=cmap, alpha=alpha, app=app, position=position)
        self._update()
        
    def filter_nogui(self, conditions):
        """
        Filters the masks based on a set of conditions with respect to the mask
        characteristics. No interactive window opens. Conditions are passed as a
        dictionary with the following possible keys:
        
        - max_area
        - min_area
        - max_intensity
        - min_intensity
        - max_eccentricity
        - min_eccentricity
        - max_solidity
        - min_solidity
        - overlap
        - overlapping_masks
        """
        filter_nogui(self, conditions)
        
    def export_filtered_characteristics(self):
        """
        Exports the characteristics of the masks that passed the filtering conditions as
        a .csv file.
        """
        for image in self:
            image.export_filtered_characteristics()

    def export_filtered_masks_png(self, cmap="default",alpha=0.3):
        """
        Exports an image of the masks that passed the filtering conditions as a .png
        file.
        """
        for image in self:
            image.export_filtered_masks_png(cmap=cmap,alpha=alpha)

    def export_filtered_masks_tif(self):
        """
        Exports an image of the masks that passed the filtering conditions as a .tif
        file.
        """
        for image in self:
            image.export_filtered_masks_tif()

    def export_filtered_masks_binary(self):
        """
        Exports an image of the masks that passed the filtering conditions as a binary 
        .tif file.
        """
        for image in self:
            image.export_filtered_masks_binary()

    def export_filtered_masks_numpy(self):
        """
        Exports the masks that passed the filtering conditions as a compressed .npz
        file. Can be loaded again with:
        
        import numpy as np
        masks = np.load('filename.npz')['array']
        """
        for image in self:
            image.export_filtered_masks_numpy()

    def export_all(self):
        for image in self:
            image.export_all()
        
    def overview(
        self, 
        characteristics=["area"],
        save_as=None,
        cmap="default",
        alpha=0.3,
        bin_list=None, 
        timestamp=False,
        save_csv=False,
        show_all_figures=True,
    ):
        """
        Produces and saves an overview .pdf file showing the segmentation and histograms
        of selected characteristics.
        """
        if characteristics == ["all"]:
            characteristics = [
                "area",
                "area_convex",
                "axis_major_length",
                "axis_minor_length",
                "eccentricity",
                "equivalent_diameter_area",
                "extent",
                "feret_diameter_max",
                "intensity_max",
                "intensity_mean",
                "intensity_min",
                "orientation",
                "perimeter",
                "perimeter_crofton",
                "solidity",
                "overlap",
            ]

        for n, prop in enumerate(characteristics):
            if prop == "intensity":
                characteristics[n] = "intensity_mean"
            elif prop == "diameter":
                characteristics[n] = "equivalent_diameter_area"
            elif prop == "max diameter":
                characteristics[n] = "feret_diameter_max"
            elif prop == "crofton perimeter":
                characteristics[n] = "perimeter_crofton"
            elif prop == "convex area":
                characteristics[n] = "area_convex"

        dfs = []
        imagenumber = 1
        for image in self:
            df_filtered = copy(image.cha[image.cha["passed_filter"]])
            df_filtered["imagename"] = image.cha.attrs["title"]
            df_filtered["imagenumber"] = imagenumber
            imagenumber += 1
            dfs.append(df_filtered)
        df = pd.concat(dfs)

        if bin_list is None:
            bin_list = ["auto"] * len(characteristics)

        unit = df["unit"].to_list()[0]
        unit2 = unit + "$^2$" if unit != "px" else unit
        name_dict = {
            "area": f"area ({unit2})",
            "area_convex": f"convex area ({unit2})",
            "eccentricity": "eccentricity",
            "solidity": "solidity",
            "intensity_mean": "mean intensity",
            "overlap": "overlap (px)",
            "equivalent_diameter_area": f"area equivalent diameter ({unit})",
            "feret_diameter_max": f"Max diameter (Feret) ({unit})",
            "orientation": "orientation",
            "perimeter": f"perimeter ({unit})",
            "perimeter_crofton": f"crofton perimeter ({unit})",
            "axis_major_length": f"Major axis length ({unit})",
            "axis_minor_length": f"Minor axis length ({unit})",
            "extent": "Ratio of pixels in the mask the pixels in the bounding box",
            "intensity_max": "Max intensity of the mask",
            "intensity_min": "minimum intensity of the mask",
            "overlap": f"amount of overlap ({unit2})",
        }
        figs = []
        for n, prop in enumerate(characteristics):
            fig, ax = plt.subplots(figsize=(11.7, 8.3))
            ax.set_xlabel(name_dict.get(prop).capitalize(), fontsize=16)
            ax.set_title(f"Histogram of {name_dict.get(prop)} for all images", fontsize=18)
            df[prop].hist(bins=bin_list[n], ax=ax, edgecolor="k", color="#0081C6")
            ax.grid(False)
            ax.set_ylabel("Count", fontsize=16)
            ax.tick_params(axis="both", which="major", labelsize=14)
            data = df[prop]
            mean = np.mean(data)
            median = np.median(data)
            std_dev = np.std(data)
            variance = np.var(data)
            skewness = scipy.stats.skew(data)
            kurtosis = scipy.stats.kurtosis(data)
            data_range = np.ptp(data)
            q1 = np.percentile(data, 25)
            q3 = np.percentile(data, 75)
            iqr = scipy.stats.iqr(data)
            minimum = np.min(data)
            maximum = np.max(data)
            count = len(data)
            total_sum = np.sum(data)
            coeff_variation = std_dev / mean

            def format_value(val):
                if val == 0:
                    return 0
                elif val < 10:
                    return f"{val:.2f}"
                elif 10 <= val < 100:
                    return f"{val:.1f}"
                elif 100 <= val:
                    return f"{int(val)}"

            x_r = 1 - len(f"Upper quantile: {format_value(q3)}") * 0.0108
            x_m = (
                x_r - 0.025 - len(f"Sum: {format_value(total_sum)}") * 0.0108
                if total_sum > 100000000
                else x_r - 0.155
            )
            x_l = (
                x_m - 0.055 - len(f"Sum: {format_value(variance)}") * 0.0108
                if variance > 1000000000000
                else x_m - 0.22
            )

            stats_text_left = (
                f"Mean: {format_value(mean)}\nStd Dev: {format_value(std_dev)}\n"
                f"Median: {format_value(median)}\nVariance: {format_value(variance)}\n"
                f"Coeff of Variation: {format_value(coeff_variation)}\n"
                f"Total number of masks: {len(df['area'].to_list())}"
            )

            stats_text_middle = (
                f"Skewness: {format_value(skewness)}\nKurtosis: {format_value(kurtosis)}\n"
                f"Count: {count}\nSum: {format_value(total_sum)}\nIQR: {format_value(iqr)}"
            )

            stats_text_right = (
                f"Lower quantile: {format_value(q1)}\nUpper quantile: {format_value(q3)}\n"
                f"Min: {format_value(minimum)}\nMax: {format_value(maximum)}\n"
                f"Range: {format_value(data_range)}"
            )
            n = "i" * int((194 * (1 - x_l + 0.011)))

            text = f"{n}\n{n}\n{n}\n{n}\n{n}\n{n}"
            text_properties = {
                "fontsize": 12,
                "color": "none",
                "verticalalignment": "top",
                "bbox": dict(
                    boxstyle="round,pad=0.3",
                    edgecolor="black",
                    facecolor="white",
                    alpha=0.5,
                ),
            }

            plt.text(x_l, 0.98, text, transform=plt.gca().transAxes, **text_properties)
            for x, txt in zip([x_l,x_m,x_r],[stats_text_left,stats_text_middle,stats_text_right]):
                plt.text(
                    x, 0.98,
                    txt,
                    ha="left",
                    va="top",
                    transform=plt.gca().transAxes,
                    fontsize=12,
                )
            
            figs.append(fig)
        
        for image in self:
            figs.append(image._make_overview_figure(cmap=cmap,alpha=alpha))

        if timestamp:
            d = datetime.now()
            stamp = f"_{d.year}{d.month}{d.day}_{d.hour}{d.minute}{d.second}"
        else:
            stamp = ""
        
        parent_folder = Path(self[0].filepath).parent
        
        if save_as is None:
            filepath = parent_folder / f"NP-SAM_results/NP-SAM_overview{stamp}.pdf"
        else:
            filepath = Path(save_as)
        filepath.parent.mkdir(exist_ok=True)
        p = PdfPages(filepath)

        for fig in figs:
            fig.savefig(p, format="pdf")
            
        if save_csv:
            file_p = Path(filepath.as_posix().split('.')[0]+"_filtered_dataframe.csv")
            first_column = df.pop("imagename")
            second_column = df.pop("imagenumber")
            df.insert(0, "imagename", first_column)
            df.insert(1, "imagenumber", second_column)
            df.to_csv(file_p, encoding="utf-8", header="true", index=False)

        p.close()
        
        if show_all_figures:
            plt.show()
        else:
            for fig in figs:
                plt.close(fig)
            if platform.system() == 'Darwin':       # macOS
                subprocess.call(('open', filepath))
            elif platform.system() == 'Windows':    # Windows
                os.startfile(filepath)
            else:                                   # linux variants
                subprocess.call(('xdg-open', filepath))


def filter(images, cmap="default", alpha=0.3, app=False, position=None):
    if not app:
        original_backend = matplotlib.get_backend()
        if original_backend != "QtAgg":
            try:
                #matplotlib.use("QtAgg") # For some reason this doesn't work
                get_ipython().magic('matplotlib qt')
                print("Matplotlib backend was set to 'qt'.")
            except:
                print("Could not set matplotlib backend to 'qt'.")
                
    images = NPSAM(images) if not isinstance(images, NPSAM) else images
    filtergui = ImageFilter(images, app=app,position=position, cmap=cmap, alpha=alpha)
    filtergui.filter()

class ImageFilter:
    def __init__(
        self,
        images,
        cmap="default",
        alpha=0.3,
        app=False,
        position=None,
    ):
        # Set all kinds of variables
        self.images = NPSAM(images) if not isinstance(images, NPSAM) else images
        self.image_index = 0
        self.app = app
        if self.app is True:
            matplotlib.use("tkagg")
        self.position = position
        self.cmap = cmap
        self.alpha = alpha
        self.buttons = {}
        self.overlapping_masks_dict = {"0": 0, "1": 1, "2": 2, "∞": np.inf}
        self.pressed_keys = set()
        self.slider_color = "#65B6F3"
        self.radio_color = "#387FBE"
        self.fig = None
        self.sliders = {}
        self.val_text = {}

        self.directory = Path(__file__).resolve().parent / "button_images"
        self.characteristics_for_filtering = [
            "area",
            "solidity",
            "intensity_mean",
            "eccentricity",
            "overlap",
        ]
        self.characteristics_format = {
            "area": "Area (px)",
            "solidity": "Solidity",
            "intensity_mean": "Intensity",
            "eccentricity": "Eccentricity",
            "overlap": "Overlap",
        }

    def apply_filters(self):
        self.cha["passed_filter"] = (
            (self.cha["area"] >= self.conditions.get_item("area")[0])
            & (self.cha["area"] <= self.conditions.get_item("area")[1])
            & (self.cha["solidity"] >= self.conditions.get_item("solidity")[0])
            & (self.cha["solidity"] <= self.conditions.get_item("solidity")[1])
            & (self.cha["intensity_mean"] >= self.conditions.get_item("intensity_mean")[0])
            & (self.cha["intensity_mean"] <= self.conditions.get_item("intensity_mean")[1])
            & (self.cha["eccentricity"] >= self.conditions.get_item("eccentricity")[0])
            & (self.cha["eccentricity"] <= self.conditions.get_item("eccentricity")[1])
            & (self.cha["overlap"] >= self.conditions.get_item("overlap")[0])
            & (self.cha["overlap"] <= self.conditions.get_item("overlap")[1])
            & (~self.cha["mask_index"].isin(self.conditions.get_item("removed_index")))
            & (self.cha["number_of_overlapping_masks"] <= self.conditions.get_item("number_of_overlapping_masks"))
        )
        self.plot_filtered_masks()

    def plot_filtered_masks(self):
        for n, visibility in enumerate(self.cha["passed_filter"]):
            self.cs[n].set_visible(visibility)
        self.text.set_text(
            f"{(~self.cha['passed_filter']).sum()} masks removed. {self.cha['passed_filter'].sum()} remain."
        )

    def create_button(
        self, x, y, w, h, default_img_path, hover_img_path, click_action, rotate=False
    ):
        ax = plt.axes([x, y, w, h], frameon=False)
        ax.set_axis_off()

        default_img = mpimg.imread(self.directory / default_img_path)
        hover_img = mpimg.imread(self.directory / hover_img_path)
        if rotate:
            default_img = np.flipud(np.fliplr(default_img))
            hover_img = np.flipud(np.fliplr(hover_img))

        img_display = ax.imshow(default_img)

        self.buttons[ax] = {
            "default": default_img,
            "hover": hover_img,
            "display": img_display,
        }
        ax.figure.canvas.mpl_connect(
            "button_press_event",
            lambda event: self.on_button_click(event, ax, click_action),
        )
        return ax

    def on_hover(self, event):
        redraw_required = False
        for ax, img_info in self.buttons.items():
            if ax.get_visible():
                if event.inaxes == ax:
                    if not np.array_equal(
                        img_info["display"].get_array(), img_info["hover"]
                    ):
                        img_info["display"].set_data(img_info["hover"])
                        ax.draw_artist(img_info["display"])
                        redraw_required = True
                elif not np.array_equal(
                    img_info["display"].get_array(), img_info["default"]
                ):
                    img_info["display"].set_data(img_info["default"])
                    ax.draw_artist(img_info["display"])
                    redraw_required = True
        if redraw_required:
            if self.app is False:
                self.fig.canvas.update()
            else:
                self.fig.canvas.draw_idle()

    def on_button_click(self, event, ax, action):
        if event.inaxes == ax:
            action()

    def on_key_press(self, event):
        slider = self.last_interacted_slider
        low, high = slider.val
        self.pressed_keys.add(event.key)

        step = 0.001*(slider.valmax-slider.valmin)
        if "shift" in self.pressed_keys:
            step = 0.01*(slider.valmax-slider.valmin)
        elif ("ctrl" in self.pressed_keys) or ("control" in self.pressed_keys):
            step = 0.1*(slider.valmax-slider.valmin)
        
        if event.key in {"up", "shift+up", "ctrl+up"}:
            val = (low + step, high)
            slider.set_val(val)
        elif event.key in {"down", "shift+down", "ctrl+down"}:
            val = (low - step, high)
            slider.set_val(val)
        elif event.key in {"right", "shift+right", "ctrl+right"}:
            val = (low, high + step)
            slider.set_val(val)
        elif event.key in {"left", "shift+left", "ctrl+left"}:
            val = (low, high - step)
            slider.set_val(val)

        if event.key == "z":
            self.return_last_removed()
        elif event.key == "a":
            self.return_all_removed()
        elif event.key == "enter":
            if self.image_index < len(self.filepaths)-1:
                self.update_next()
            else:
                self.final_save()
        elif event.key == "backspace":
            if self.image_index != 0:
                self.update_previous()

    def on_key_release(self, event):
        if event.key in self.pressed_keys:
            self.pressed_keys.remove(event.key)

    def on_click(self, event):
        if event.inaxes == self.ax_filtered:
            for idx, row in self.cha[self.cha["passed_filter"]].iterrows():
                if (
                    row["bbox-1"] <= event.xdata <= row["bbox-3"]
                    and row["bbox-0"] <= event.ydata <= row["bbox-2"]
                ):
                    self.conditions.get_item("removed_index").append(idx)
                    self.apply_filters()
                    self.fig.canvas.draw()
                    break

    def return_all_removed(self):
        self.conditions.set_item("removed_index", [])
        self.apply_filters()
        self.fig.canvas.draw()

    def return_last_removed(self):
        try:
            self.conditions.get_item("removed_index").pop()
            self.apply_filters()
            self.fig.canvas.draw()
        except IndexError:
            pass

    def final_save(self):
        self.apply_filters()
        plt.close(self.fig)

    def update_next(self):
        self.apply_filters()

        self.image_index += 1
        
        if self.app:
            self.position = self.fig.canvas.manager.window.wm_geometry()
        else:
            self.position = self.fig.canvas.manager.window.geometry()

        self.filter()

    def update_previous(self):
        self.apply_filters()

        self.image_index -= 1
        
        if self.app:
            self.position = self.fig.canvas.manager.window.wm_geometry()
        else:
            self.position = self.fig.canvas.manager.window.geometry()

        self.filter()

    def create_slider(self, characteristic):
        ax = self.slider_axes[characteristic]
        
        slider = RangeSlider(
            ax,
            "",
            valmin=self.cha[characteristic].min(),
            valmax=self.cha[characteristic].max(),
            valinit=self.conditions.get_item(characteristic),
        )
        slider.on_changed(lambda val: self.update_slider(val, characteristic))
        slider.valtext.set_visible(False)
        self.sliders[characteristic] = slider

        self.val_text[characteristic] = ax.text(
            0,
            1.12,
            f"{self.characteristics_format[characteristic]}: ({self.conditions.get_item(characteristic)[0]:.5g}, {self.conditions.get_item(characteristic)[1]:.5g})",
            fontsize=14,
            ha="left",
            va="center",
            transform=ax.transAxes,
        )

    def update_slider(self, val, characteristic):
        self.last_interacted_slider = self.sliders[characteristic]
        self.conditions.set_item(characteristic, val)

        self.val_text[characteristic].set_text(
            f"{self.characteristics_format[characteristic]}: ({self.conditions.get_item(characteristic)[0]:.5g}, {self.conditions.get_item(characteristic)[1]:.5g})",
        )

        self.apply_filters()

    def create_overlapping_masks_radio(self, ax):
        ax.set_aspect("equal")
        valinit = self.conditions.get_item("number_of_overlapping_masks")
        if type(valinit) == str or valinit > 2:
            valinit = 3
        self.radio_overlapping_masks = RadioButtons(
            ax,
            ("0", "1", "2", "∞"),
            active=valinit,
            activecolor=self.radio_color,
        )

        dists = [0, 0.12, 0.2245, 0.325]
        for i, (circle, label) in enumerate(
            zip(
                self.radio_overlapping_masks.circles,
                self.radio_overlapping_masks.labels,
            )
        ):
            new_x = 0.53 + dists[i]
            new_y = 0.5
            circle.set_center((new_x, new_y))
            circle.set_radius(0.02)
            label.set_position((new_x + 0.03, new_y))
            label.set_fontsize(14)

        self.overlapping_masks_val_text = ax.text(
            0,
            0.5,
            "Number of \noverlapping masks:",
            fontsize=14,
            ha="left",
            va="center",
            transform=ax.transAxes,
        )

        self.radio_overlapping_masks.on_clicked(self.update_overlapping_masks)
        
    def update_overlapping_masks(self, label):
        self.conditions.set_item("number_of_overlapping_masks", self.overlapping_masks_dict[label])
        self.apply_filters()
        self.fig.canvas.draw()

    def initiate_filter_values(self):
        for characteristic in self.characteristics_for_filtering:
            if not self.seg.metadata.has_item(f"Filtering.Conditions.{characteristic}"):
                self.seg.metadata.set_item(
                    f"Filtering.Conditions.{characteristic}",
                    (self.cha[characteristic].min(),self.cha[characteristic].max())
                )
        if not self.seg.metadata.has_item("Filtering.Conditions.number_of_overlapping_masks"):
            self.seg.metadata.set_item("Filtering.Conditions.number_of_overlapping_masks",np.inf)
        if not self.seg.metadata.has_item("Filtering.Conditions.removed_index"):
            self.seg.metadata.set_item("Filtering.Conditions.removed_index",[])
        self.conditions = self.seg.metadata.get_item("Filtering.Conditions")
    
    def create_figure(self):
        self.fig = plt.figure(figsize=(8,8))
        
        self.ax_img = plt.axes([0, 0.51, 0.5, 0.41])
        self.ax_all = plt.axes([0.5, 0.51, 0.5, 0.41],sharex=self.ax_img,sharey=self.ax_img)
        self.ax_filtered = plt.axes([0, 0.05, 0.5, 0.41],sharex=self.ax_img,sharey=self.ax_img)
        
        if self.app:
            self.fig.canvas.manager.window.wm_geometry(self.position)
        else:
            try:
                self.fig.canvas.manager.window.setGeometry(self.position)
            except:
                pass
        
        # Create axes for sliders and radiobuttons
        self.slider_axes = {
            c: plt.axes([0.525, 0.430-n*0.055, 0.45, 0.03], fc=self.slider_color, zorder=1)
            for n,c in enumerate(self.characteristics_for_filtering)
        }
        self.ax_radio_overlapping_masks = plt.axes(
            [0.525, -0.12, 0.5, 0.6], frameon=False
        )

        # Create buttons
        self.close_and_save_button = self.create_button(
            0.835,
            0.01,
            0.14,
            0.085,
            "Save_close.png",
            "Save_close_dark.png",
            self.final_save,
        )

        self.next_button = self.create_button(
            0.68, 0.01, 0.14, 0.085, "arrow.png", "arrow_dark.png", self.update_next
        )

        self.previous_button = self.create_button(
            0.525,
            0.01,
            0.14,
            0.085,
            "arrow.png",
            "arrow_dark.png",
            self.update_previous,
            rotate=True,
        )

        self.plus_one_button = self.create_button(
            0.1,
            0.0,
            0.10,
            0.05,
            "plus_one.png",
            "plus_one_dark.png",
            self.return_last_removed,
        )

        self.plus_all_button = self.create_button(
            0.3,
            0.0,
            0.10,
            0.05,
            "plus_all.png",
            "plus_all_dark.png",
            self.return_all_removed,
        )

        self.text = self.fig.text(
            0.752, 0.12, "", fontsize=16, horizontalalignment="center"
        )

        self.fig.suptitle("", fontsize=16)

        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)
        self.fig.canvas.mpl_connect("key_release_event", self.on_key_release)
        self.fig.canvas.mpl_connect("button_press_event", self.on_click)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_hover)
        
        plt.show()

    def filter(self, image_index = None):
        if not image_index is None:
            self.image_index = image_index

        self.NPSAMImage = self.images[self.image_index]
        self.img = self.NPSAMImage.img
        self.seg = self.NPSAMImage.seg
        self.cha = self.NPSAMImage.cha
        self.contours = self.seg.metadata.Filtering.Contours.as_dictionary()
        self.initiate_filter_values()

        if self.fig is None:
            self.create_figure()
        self.fig.show()
        
        self.all_axes = ([self.ax_img, self.ax_all, self.ax_filtered] + 
            [self.slider_axes[key] for key in self.slider_axes] +
            [self.ax_radio_overlapping_masks])
        for ax in self.all_axes:
            ax.cla()

        string_title = (
            f"{self.image_index+1}/{len(self.images)} - {self.img.metadata.General.title}"
            if len(self.images) > 1
            else self.img.metadata.General.title
        )
        self.fig.suptitle(string_title, fontsize=16)

        im_titles = ["Image","All masks", "Filtered masks"]
        for ax, title in zip([self.ax_img,self.ax_all,self.ax_filtered],im_titles):
            ax.imshow(self.img.data, cmap="gray")
            ax.set_title(title)
            ax.axis("off")

        alpha=0.3
        _ = plot_masks(self.NPSAMImage, self.ax_all, alpha=self.alpha, cmap=self.cmap)
        self.cs = plot_masks(self.NPSAMImage, self.ax_filtered, alpha=self.alpha, cmap=self.cmap)

        self.characteristics_format["area"] = f"Area ({self.cha['unit'][0]}$^2$)"
        # Create sliders
        for characteristic in self.characteristics_for_filtering:
            self.create_slider(characteristic)
        self.last_interacted_slider = self.sliders["area"]
        # Create radio buttons
        self.create_overlapping_masks_radio(self.ax_radio_overlapping_masks)

        if self.image_index < len(self.images)-1:
            self.next_button.set_visible(True)
        else:
            self.next_button.set_visible(False)
        if self.image_index != 0:
            self.previous_button.set_visible(True)
        else:
            self.previous_button.set_visible(False)

        self.apply_filters()
        self.fig.canvas.draw()


def filter_nogui(images, conditions):
    """
    Filters the masks based on a set of conditions with respect to the mask
    characteristics. No interactive window opens. Conditions are passed as a 
    dictionary with the following possible keys:
    
    - area: tuple with min and max values
    - intensity: tuple with min and max values
    - eccentricity: tuple with min and max values
    - solidity: tuple with min and max values
    - overlap: tuple with min and max values
    - overlapping_masks: integer designating maximum number of overlapping masks
    """
    images = NPSAM(images) if not isinstance(images, NPSAM) else images

    if type(conditions) == dict:
        conditions = [conditions] * len(images)
        if len(images) > 1:
            print("The filtering conditions will be used for all images.")
    elif type(conditions) == list:
        if len(conditions) == len(images):
            for entry in conditions:
                if type(entry) != dict:
                    raise ValueError((
                        "The list entries must be dictionaries containing the filter ",
                        "conditions."
                    ))
        elif len(conditions) == 1:
            conditions = conditions * len(images)
            print("The filtering conditions will be used for all images.")
        else:
            raise ValueError((
                "The length of the list with filtering conditions does not have the ",
                "same length as the list with images."
            ))

    for image, filter_conditions in zip(images, conditions):
        cha = image.cha
        filters = {
            "area": (math.floor(cha["area"].min()), math.ceil(cha["area"].max())),
            "solidity": (0, 1),
            "intensity_mean": (math.floor(cha["intensity_mean"].min()), math.ceil(cha["intensity_mean"].max())),
            "eccentricity": (0, 1),
            "overlap": (0,np.inf),
            "number_of_overlapping_masks": np.inf,
            "removed_index": []
        }

        filters.update(filter_conditions)

        cha["passed_filter"] = (
            (cha["area"] >= filters["area"][0])
            & (cha["area"] <= filters["area"][1])
            & (cha["solidity"] >= filters["solidity"][0])
            & (cha["solidity"] <= filters["solidity"][1])
            & (cha["intensity_mean"] >= filters["intensity_mean"][0])
            & (cha["intensity_mean"] <= filters["intensity_mean"][1])
            & (cha["eccentricity"] >= filters["eccentricity"][0])
            & (cha["eccentricity"] <= filters["eccentricity"][1])
            & (cha["overlap"] >= filters["overlap"][0])
            & (cha["overlap"] <= filters["overlap"][1])
            & (cha["number_of_overlapping_masks"] <= filters["number_of_overlapping_masks"])
            & (~cha["mask_index"].isin(filters["removed_index"]))
        )

        image.seg.metadata.set_item("Filtering.Conditions", filters)