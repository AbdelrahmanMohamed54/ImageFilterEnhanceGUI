"""

Author: Abdelrahman Mohamed (22201965)

File description: Gaussian Blur Filter implementation

"""

import cv2
import numpy as np


def gaussian_kernel(kernel_size, sigma):
    # Create a 2D Gaussian kernel
    kernel = np.fromfunction(lambda x, y: (1 / (2 * np.pi * sigma * 2)) * np.exp(
        -((x - kernel_size // 2) ** 2 + (y - kernel_size // 2) ** 2) / (2 * sigma * 2)), (kernel_size, kernel_size))

    # Normalize the kernel
    kernel = kernel / np.sum(kernel)

    return kernel


def guassian_blur(image, kernel_size, sigma):
    # Create a Gaussian kernel
    kernel = gaussian_kernel(kernel_size, sigma)

    # Pad the image to handle kernel size and boundaries
    padded_image = np.pad(image, ((kernel_size // 2, kernel_size // 2), (kernel_size // 2, kernel_size // 2)),
                          mode='constant')

    # Create an empty output image
    output_image = np.zeros_like(image)

    # Apply the Gaussian kernel to each pixel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            output_image[i, j] = apply_kernel(padded_image[i:i + kernel_size, j:j + kernel_size], kernel)

    return output_image


def apply_kernel(image_patch, kernel):
    # Apply the kernel to the image patch
    return np.sum(image_patch * kernel)


def gaussian_blur(image, kernel_size, sigma):

    blurred_image = cv2.GaussianBlur(image, kernel_size, sigma)
    return blurred_image
