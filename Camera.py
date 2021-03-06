#pip install opencv-python

import cv2
import numpy as np


# (1)cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# (0)cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# (-1)cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

img = cv2.imread('123.jpg',1)
cv2.imshow('image0',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

vedio_capture = cv2.VideoCapture(0)

if not vedio_capture.isOpened():
    raise Exception("Coud not find vedio device")
else:
    while(True):
        # 從攝影機擷取一張影像
        ret, frame = vedio_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 顯示圖片
        cv2.imshow('frame', gray)
          
        # 若按下 q 鍵則離開迴圈
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    # 釋放攝影機
    vedio_capture.release()

    # 關閉所有 OpenCV 視窗
    cv2.destroyAllWindows()
