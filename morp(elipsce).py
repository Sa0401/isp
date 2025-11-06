import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# Load grayscale image 
img = cv2.imread("C:/Users/asus/Downloads/sample_image.jpg", 0) 
# Different filters 
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) 
ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)) 
cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5)) 
# Apply dilation with different kernels 
dilate_rect = cv2.dilate(img, rect_kernel, iterations=1) 
dilate_ellipse = cv2.dilate(img, ellipse_kernel, iterations=1) 
dilate_cross = cv2.dilate(img, cross_kernel, iterations=1) 
# Show results 
plt.figure(figsize=(12,6)) 
plt.subplot(141), plt.imshow(img, cmap='gray'), plt.title("Original") 
plt.subplot(142), plt.imshow(dilate_rect, cmap='gray'), plt.title("Rect Kernel") 
plt.subplot(143), plt.imshow(dilate_ellipse, cmap='gray'), plt.title("Ellipse Kernel") 
plt.subplot(144), plt.imshow(dilate_cross, cmap='gray'), plt.title("Cross Kernel") 
plt.tight_layout() 
plt.show()