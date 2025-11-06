import cv2, zlib, numpy as np

# Read grayscale image
img = cv2.imread(r"C:/Users/asus/Downloads/sample_image.jpg", 0)

# Convert image to bytes
img_bytes = img.tobytes()

# Compress using zlib (uses Huffman coding internally)
compressed = zlib.compress(img_bytes)

# Decompress
decompressed = zlib.decompress(compressed)
decoded = np.frombuffer(decompressed, dtype=np.uint8).reshape(img.shape)

# Show compression details
print("Original size:", len(img_bytes))
print("Compressed size:", len(compressed))
print("Compression ratio: %.2f%%" % (len(compressed) / len(img_bytes) * 100))

# Show images
cv2.imshow("Original", img)
cv2.imshow("Decoded", decoded)
cv2.waitKey(0)
cv2.destroyAllWindows()
