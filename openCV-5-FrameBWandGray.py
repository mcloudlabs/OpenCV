import cv2
print (cv2.__version__)
import numpy as np

while True:
    frame =np.zeros([250,250],dtype=np.uint8)
    frame[:125,0:125]=255
    cv2.imshow('myWindow', frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
