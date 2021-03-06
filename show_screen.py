import numpy as np
import cv2
from PIL import ImageGrab

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("output", 800, 600)

while True:
    img = ImageGrab.grab() #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("output", frame)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break
    