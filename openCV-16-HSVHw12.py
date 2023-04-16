import cv2
import numpy as np

print (cv2.__version__)

width =640 #width ideally keep it on standard sizing 640x480 1280x720
height=360 #height ideally keep it on standard sizing 640x480 1280x720
x=np.zeros([256,720,3],dtype= np.uint8)
y=np.zeros([256,720,3],dtype= np.uint8)

for row in range (0,256,1):
    for column in range (0,720,1):
        x[row,column]=(int(column/4),row,255)
x=cv2.cvtColor(x,cv2.COLOR_HSV2BGR)

for row in range (0,256,1):
    for column in range (0,720,1):
        y[row,column]=(int (column/4),255,row)
y=cv2.cvtColor(y,cv2.COLOR_HSV2BGR)

while True:

    cv2.imshow('colorPicker',x)
    cv2.moveWindow('colorPicker',0,0)
    cv2.imshow('colorPickerY',y)
    cv2.moveWindow('colorPickerY',0,(height +30))

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
