import cv2
print (cv2.__version__)
import numpy as np

while True:
    frame =np.zeros([250,250,3],dtype=np.uint8) # create the Array with 3 tuples
    frame[:125,0:125]=(0,0,255)
    frame[:,125:255]=(0,255,0)
    cv2.imshow('myWindow', frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
