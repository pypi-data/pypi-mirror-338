import cv2
import numpy as np

def Sketch(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection with lower threshold for more edges
    edges = cv2.Canny(blurred, 10, 80)

    # Dilate edges to make them thicker
    kernel = np.ones((1,1), np.uint8)
    thick_edges = cv2.dilate(edges, kernel, iterations=1)

    # Invert edges for sketch effect
    inverted_edges = cv2.bitwise_not(thick_edges)

    # ----- SHADING EFFECT -----
    # Invert grayscale image
    inverted_gray = cv2.bitwise_not(gray)

    # Blur the inverted image
    shading = cv2.GaussianBlur(inverted_gray, (25,25), 0)

    # Blend shading with original grayscale image
    shaded = cv2.divide(gray, 255 - shading, scale=256)

    # Combine edges and shading
    final_sketch = cv2.bitwise_and(shaded, inverted_edges)

    return final_sketch

