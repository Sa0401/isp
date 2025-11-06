import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:/Users/asus/Downloads/sample_image.jpg", 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
ahe_img = clahe.apply(img)

plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(ahe_img, cmap='gray'), plt.title('AHE (CLAHE)'), plt.axis('off')
plt.show()