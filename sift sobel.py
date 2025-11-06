import cv2

# Read image
img = cv2.imread(r"C:/Users/asus/Downloads/sample_image.jpg", 0)

# SIFT feature detection
sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(img, None)
sift_img = cv2.drawKeypoints(img, kp, None, (0,255,0))

# Sobel edge detection
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.convertScaleAbs(cv2.magnitude(sobelx, sobely))

# Display results
cv2.imshow('Original', img)
cv2.imshow('SIFT Features', sift_img)
cv2.imshow('Sobel Edges', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
