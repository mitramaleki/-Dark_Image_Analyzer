from typing import List

import numpy as np
import matplotlib.pyplot as plt

"""
This class is for analyzing dark images.
Dark frames are images obtained by taking images with a closed lens cap.
They do not contain any real image information but merely consist of sensor noise.
"""


class DarkImage:

    def __init__(self, images: List[np.ndarray]):
        self.images: List[np.ndarray] = images
        self.stacked_images: np.ndarray = np.stack(images)
        self.median_array: np.ndarray = self.get_median_array(self.stacked_images)
        self.mean_array: np.ndarray = self.get_mean_array(self.stacked_images)
        self.std_array: np.ndarray = self.get_std_array(self.stacked_images)

    @classmethod
    def get_median_array(cls, stacked_images):
        return np.median(stacked_images, axis=0)

    @classmethod
    def get_mean_array(cls, stacked_images):
        return np.mean(stacked_images, axis=0)

    @classmethod
    def get_std_array(cls, stacked_images):
        return np.std(stacked_images, axis=0)

    def get_sigma_clipped(self, std_count: int = 3) -> np.ndarray:
        dark_image_shape = self.stacked_images.shape[1], self.stacked_images.shape[2]
        sigma_clipped_dark = np.zeros(shape=dark_image_shape)
        for j in range(self.stacked_images.shape[1]):
            for k in range(self.stacked_images.shape[2]):
                pixel_values = []
                for i in range(self.stacked_images.shape[0]):
                    pixel_value = self.stacked_images[i][j][k]
                    pixel_median = self.median_array[j][k]
                    pixel_std = self.std_array[j][k]
                    if (
                            pixel_median + std_count * pixel_std
                    ) > pixel_value > (
                            pixel_median - std_count * pixel_std
                    ):
                        pixel_values.append(pixel_value)
                if pixel_values:
                    # write mean or median based on preference:
                    sigma_clipped_dark[j][k] = np.median(pixel_values)
        return sigma_clipped_dark

    def draw_histogram(self, bin_range_max) -> None:
        data = self.get_sigma_clipped()
        # put exposure time as title:
        # write mean or median based on preference:
        title = '30-median'
        file_path = 'data/' + title + '.png'
        plt.clf()
        bins_list = list(map(lambda x: x * 0.1, range(bin_range_max * 2)))
        counts, bins = np.histogram(data, bins=bins_list)
        plt.hist(bins[:-1], bins, weights=counts)
        plt.title(title)
        plt.savefig(file_path)
        # write mean or median based on preference:
        print(np.median(data))


