import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
img = cv2.imread(r"C:/Users/asus/Downloads/sample_image.jpg", 0)

# Apply Laplacian filter
lap = cv2.Laplacian(img, cv2.CV_64F)

# Sharpened image = original + (-1 * Laplacian)
sharp = cv2.convertScaleAbs(img - lap)

# Display results
plt.subplot(1,3,1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.axis('off')
plt.subplot(1,3,2), plt.imshow(lap, cmap='gray'), plt.title('Laplacian'), plt.axis('off')
plt.subplot(1,3,3), plt.imshow(sharp, cmap='gray'), plt.title('Sharpened'), plt.axis('off')
plt.show()
