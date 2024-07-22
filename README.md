

# Dark Image Analysis Tool

## Overview

This tool is designed for analyzing dark frames in astrophotography. Dark frames are images taken with a closed lens cap to capture sensor noise without any real image information. This tool helps in analyzing such frames by computing statistical measures like median, mean, and standard deviation, and by applying sigma clipping to reduce noise.

## Features

- Computes the median, mean, and standard deviation arrays from a stack of dark images.
- Applies sigma clipping to the dark images to reduce noise.
- Generates and saves histograms of the sigma-clipped dark images.

## Dependencies

- `numpy`: For numerical operations.
- `matplotlib`: For generating histograms.

You can install these dependencies using the following command:

```sh
pip install numpy matplotlib
```

## Usage

1. Clone the repository:

```sh
git clone https://github.com/yourusername/dark-image-analysis-tool.git
cd dark-image-analysis-tool
```

2. Create and analyze dark images using the `DarkImage` class:

```python
from dark_image import DarkImage
import numpy as np

# Example list of dark images (replace with your actual dark images)
dark_images = [np.random.normal(size=(100, 100)) for _ in range(30)]

# Create a DarkImage object
dark_image_analyzer = DarkImage(dark_images)

# Get the median array
median_array = dark_image_analyzer.median_array

# Get the mean array
mean_array = dark_image_analyzer.mean_array

# Get the standard deviation array
std_array = dark_image_analyzer.std_array

# Apply sigma clipping
sigma_clipped_array = dark_image_analyzer.get_sigma_clipped()

# Draw and save a histogram of the sigma-clipped array
dark_image_analyzer.draw_histogram(bin_range_max=50)
```

## Example Output

The script generates and saves a histogram of the sigma-clipped dark image data as `data/30-median.png`.

## How It Works

### DarkImage Class

- **Initialization**: Takes a list of dark images and computes the stacked images, median, mean, and standard deviation arrays.
- **Median Array**: `get_median_array` computes the median of the stacked images along the first axis.
- **Mean Array**: `get_mean_array` computes the mean of the stacked images along the first axis.
- **Standard Deviation Array**: `get_std_array` computes the standard deviation of the stacked images along the first axis.
- **Sigma Clipping**: `get_sigma_clipped` applies sigma clipping to reduce noise based on a specified standard deviation count.
- **Histogram**: `draw_histogram` generates and saves a histogram of the sigma-clipped data.
