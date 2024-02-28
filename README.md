# ImageFilterEnhanceGUI

## Overview

ImageFilterEnhanceGUI is a Python program that provides a user-friendly graphical user interface (GUI) for applying various image filters and enhancements. This project aims to simplify image processing tasks by allowing users, including both programmers and non-programmers, to easily apply filters such as Gaussian blur, Canny edge detection, and sharpening to images.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- OpenCV (cv2)
- NumPy
- Pillow (PIL)
- Tkinter (usually included in Python standard library)
- Matplotlib (for displaying images in Jupyter Notebook)

You can install the dependencies using pip:

```bash
pip install opencv-python numpy pillow matplotlib
```

## Running the Code

To run the program, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/ImageFilterEnhanceGUI.git
```

2. Navigate to the repository directory:

```bash
cd ImageFilterEnhanceGUI
```

3. Run the main Python script:

```bash
python CV_GUI.py
```

4. The GUI window will appear, allowing you to select an image and apply filters/enhancements.

## File Descriptions

- **main.py**: This file contains the main script for running the GUI application. It utilizes Tkinter for creating the graphical interface and connects the user interface with the image processing functions.

- **canny_edge.py**: Implements the Canny edge detection algorithm. It includes functions for calculating gradients, performing non-maximum suppression, and applying double thresholding.

- **Gaussian_blur.py**: Implements the Gaussian blur filter using a custom implementation of the Gaussian kernel. It includes functions for generating the Gaussian kernel, applying it to the image, and performing image blurring.

- **Sharpening_filter.py**: Implements the sharpening filter using both custom implementation and OpenCV's filter2D function. It includes functions for creating sharpening filter kernels and applying them to images.

## Usage

1. Launch the GUI application by running `CV_GUI.py`.
2. Load an image using the "Load Image" button.
3. Select a filter or enhancement from the dropdown menu.
4. Adjust any parameters if applicable (e.g., kernel size for Gaussian blur, sharpening factor for sharpening).
5. Click the "Apply Filter" button to apply the selected filter/enhancement.
6. The original and filtered images will be displayed side by side in the GUI window.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
