#!/usr/bin/env python

import numpy as np
import cv2
import pyautogui
#from PIL import ImageGrab
import pyscreenshot as ImageGrab #same as above but works for win+linux


cv2.namedWindow("Puzzle Solver Result", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Puzzle Solver Result", 800, 600)
cv2.namedWindow("Puzzle Solver Input", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Puzzle Solver Input", 200, 200)

def matchPiece(piece_img, full_img):

    method = cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(piece_img, full_img, method)
    mn_value,_,mn_location,_ = cv2.minMaxLoc(result)
    mn_p_x,mn_p_y = mn_location
    
    #coursor_img = cv2.cvtColor(coursor_img, cv2.COLOR_BGR2RGB)

    rows,cols = piece_img.shape[:2]
    cv2.rectangle(full_img, (mn_p_x,mn_p_y),(mn_p_x+cols,mn_p_y+rows),(0,0,255),5)
    return full_img


def getCoursorImg(radian_x = 16, radian_y=16):

    pos = pyautogui.position()
    (c_y, c_x) = pos
    
    # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
    img = ImageGrab.grab() # default multi monitor == False
    img_np = np.array(img)

    x_start = min(img_np.shape[0], max(0, c_x-radian_x))
    x_end = min(img_np.shape[0],  max(0, c_x+radian_x))
    y_start = min(img_np.shape[1],  max(0, c_y-radian_y))
    y_end = min(img_np.shape[1],  max(0, c_y+radian_y))
    if(x_start == x_end):
        x_start -= 3
    if(y_start == y_end):
        y_start -= 3

    #cv2.imwrite("debug_img.jpg", img_np)

    coursor_img = img_np[x_start:x_end, y_start:y_end, :]
    coursor_img = cv2.cvtColor(coursor_img, cv2.COLOR_BGR2RGB)

    return coursor_img


def main():
    full_image = cv2.imread("full_image.jpg")

    while True:
        piece_img = getCoursorImg()
        result_img = matchPiece(piece_img, full_image.copy())

        cv2.imshow("Puzzle Solver Result", result_img)
        cv2.imshow("Puzzle Solver Input", piece_img)
        if cv2.waitKey(1) & 0Xff == ord('q'):
            break
        if cv2.getWindowProperty("Puzzle Solver Result", cv2.WND_PROP_VISIBLE) < 1:        
            break
        if cv2.getWindowProperty("Puzzle Solver Input", cv2.WND_PROP_VISIBLE) < 1:        
            break


if __name__ == "__main__":
    main()