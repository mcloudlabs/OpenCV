import cv2
import numpy as np
print (cv2.__version__)
xVal = 0 
yVal=0
evt = 0
def mouseClick(event,xPos,yPos,flags, params):
    global evt
    global xVal 
    global yVal
    if event == cv2.EVENT_LBUTTONDOWN:
        print (event)
        evt=event
        xVal=xPos
        yVal=yPos
    if event == cv2.EVENT_LBUTTONUP:
        print (event)
        evt=event




width =1280 #width ideally keep it on standard sizing 640x480 1280x720
height=720 #height ideally keep it on standard sizing 640x480 1280x720

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.

cv2.namedWindow('myWebCam')
cv2.setMouseCallback('myWebCam',mouseClick) #throughs back 5 returns that needs to be caught by mouseClick function

while True:
    ignore, frame = cam.read() #read frame from the webcam 
    cv2.imshow('myWebCam',frame) #sShow Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen

    if evt == 1 :
        x= np.zeros([250,250,3],dtype=np.uint8)
        y=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
        clr=y[yVal][xVal] 
        print (clr)
        x[:,:] = clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
        cv2.imshow('colorPicker',x)
        cv2.moveWindow('colorPicker',width,0)
        evt =0
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()