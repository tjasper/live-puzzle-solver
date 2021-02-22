#!/usr/bin/env python

import numpy as np
import cv2
from PIL import ImageGrab
#import pyscreenshot as ImageGrab #same as above but works for win+linux
import pyautogui

offset_x = 16
offset_y = 16


pos = pyautogui.position()

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("output", 600, 600)

while True:

    pos = pyautogui.position()
    (c_x, c_y) = pos
    print(c_x, c_y)

    img = ImageGrab.grab(bbox=(c_x-offset_x, c_y-offset_y, c_x+offset_x, c_y+offset_y ))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("output", frame)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break
    if cv2.getWindowProperty("output", cv2.WND_PROP_VISIBLE) < 1:        
        break
    