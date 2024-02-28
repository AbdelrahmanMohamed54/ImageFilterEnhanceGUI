"""

Author: Abdelrahman Mohamed , 22201965

File description: Canny edge detector implementation

"""

import numpy as np
import cv2


def edge_tracking_hysteresis(suppressed, low_threshold, high_threshold):
    # Create an array to store the final edge map
    edges = np.zeros_like(suppressed)

    # Find the indices of strong edges
    strong_edge_indices = suppressed >= high_threshold

    # Set strong edges to white (255) in the output image
    edges[strong_edge_indices] = 255

    # Perform connectivity analysis to track weak edges connected to strong edges
    rows, cols = edges.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if suppressed[i, j] >= low_threshold and edges[i, j] == 0:
                # Check if there is a strong edge in the 8-neighborhood
                if np.any(edges[i - 1:i + 2, j - 1:j + 2] == 255):
                    edges[i, j] = 255

    return edges


def canny_edge(image, low_threshold, high_threshold):
    # Step 1: Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Apply Gaussian filter
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3: Calculate the intensity gradients
    gradients_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    gradients_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    gradients_magnitude = np.sqrt(gradients_x ** 2 + gradients_y ** 2)
    gradients_magnitude = np.uint8(gradients_magnitude)
    gradients_orientation = np.arctan2(gradients_y, gradients_x)

    # Step 4: Perform non-maximum suppression
    suppressed = np.zeros_like(gradients_magnitude)
    angles = gradients_orientation * (180.0 / np.pi)
    angles[angles < 0] += 180

    for i in range(1, gradients_magnitude.shape[0] - 1):
        for j in range(1, gradients_magnitude.shape[1] - 1):
            q = 255
            r = 255

            # Angle 0
            if (0 <= angles[i, j] < 22.5) or (157.5 <= angles[i, j] <= 180):
                q = gradients_magnitude[i, j + 1]
                r = gradients_magnitude[i, j - 1]
            # Angle 45
            elif 22.5 <= angles[i, j] < 67.5:
                q = gradients_magnitude[i + 1, j - 1]
                r = gradients_magnitude[i - 1, j + 1]
            # Angle 90
            elif 67.5 <= angles[i, j] < 112.5:
                q = gradients_magnitude[i + 1, j]
                r = gradients_magnitude[i - 1, j]
            # Angle 135
            elif 112.5 <= angles[i, j] < 157.5:
                q = gradients_magnitude[i - 1, j - 1]
                r = gradients_magnitude[i + 1, j + 1]

            if (gradients_magnitude[i, j] >= q) and (gradients_magnitude[i, j] >= r):
                suppressed[i, j] = gradients_magnitude[i, j]

    # Step 5: Apply double thresholding
    strong_edges = np.zeros_like(suppressed)
    weak_edges = np.zeros_like(suppressed)
    strong_edges[gradients_magnitude >= high_threshold] = 255
    weak_edges[(gradients_magnitude >= low_threshold) & (gradients_magnitude < high_threshold)] = 255

    # Step 6: Perform edge tracking by hysteresis
    edges = cv2.Canny(suppressed, low_threshold, high_threshold)
    # edges = edge_tracking_hysteresis(suppressed, low_threshold, high_threshold)

    """ 
    Note: The results of the cv2 canny module is better than the one I implemented when performing edge tracking by 
    hysteresis that's why i used it here but both work perfectly and my implementation of the edge_tracking_hysteresis 
    function is here for the completion of the code implementation (in step 6).
    """

    return edges

