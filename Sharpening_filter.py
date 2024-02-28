"""
Author: Abdelrahman Mohamed (22201965)

File description: Sharpening Filter implementation

"""


import cv2
import numpy as np


def shrapen_image(image, sharpening_factor):
    # Create the sharpening filter kernel with the specified sharpening factor
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, sharpening_factor, -1],
                                  [0, -1, 0]])

    # Get image dimensions
    height, width = image.shape[:2]
    channels = image.shape[2] if len(image.shape) == 3 else 1

    # Create a new image for storing the sharpened result
    sharpened_image = np.zeros_like(image)

    # Apply the sharpening filter
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for k in range(channels):  # Loop through each color channel (RGB)
                if channels == 1:
                    sharpened_image[i, j] = np.sum(
                        image[i - 1:i + 2, j - 1:j + 2] * sharpening_kernel
                    )
                else:
                    sharpened_image[i, j, k] = np.sum(
                        image[i - 1:i + 2, j - 1:j + 2, k] * sharpening_kernel
                    )

    # Clip the pixel values to the valid range [0, 255]
    sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

    return sharpened_image


def sharpen_image(image, sharpening_factor):
    # Create the base sharpening filter kernel
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

    # Multiply the kernel by the sharpening factor
    kernel = kernel * sharpening_factor

    # Apply the sharpening kernel to the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    return sharpened_image
