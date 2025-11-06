import cv2
import numpy as np

def draw_text(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.putText(img, 'Hello!', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 255), 2, cv2.LINE_AA)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_text)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(2) & 0xFF == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
