import cv2, heapq, numpy as np
from collections import Counter

# Read grayscale image
img = cv2.imread(r"C:/Users/asus/Downloads/sample_image.jpg", 0)

# Count pixel frequencies
freq = Counter(img.flatten())

# Build Huffman tree
heap = [[w, [s, ""]] for s, w in freq.items()]
heapq.heapify(heap)
while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    for p in a[1:]: p[1] = '0' + p[1]
    for p in b[1:]: p[1] = '1' + p[1]
    heapq.heappush(heap, [a[0]+b[0]] + a[1:] + b[1:])

# Huffman codes
codes = {a: b for a, b in heap[0][1:]}
rev = {v: k for k, v in codes.items()}

# Encode image
encoded = ''.join(codes[p] for p in img.flatten())
print("Original bits:", img.size*8)
print("Encoded bits:", len(encoded))
print("Compression ratio: %.2f%%" % (len(encoded)/(img.size*8)*100))

# Decode image
decoded, code = [], ''
for bit in encoded:
    code += bit
    if code in rev:
        decoded.append(rev[code])
        code = ''
decoded = np.array(decoded).reshape(img.shape)

# Show images
cv2.imshow('Original', img)
cv2.imshow('Decoded', decoded.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
