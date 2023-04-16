import cv2
import numpy as np
import time
print (cv2.__version__)

width =640 #width ideally keep it on standard sizing 640x480 1280x720
height=360 #height ideally keep it on standard sizing 640x480 1280x720
myRadius=30
circleColor=(0,0,0)
circleThickness=2
myText='Here it is'
myFont=cv2.FONT_HERSHEY_COMPLEX
textColor=(100,255,75)

upperLeft=(250,140)
lowerRight=(390,220)
rectColor=(0,255,0)
lineW=4

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.

tLast=time.time()
print (tLast)
fpsFilter=30
time.sleep(1)
while True:
    dT=time.time()-tLast
    print(dT)
    tLast=time.time()
    fps=int(1/dT)
    
    fpsFilter=int(fpsFilter*.9+fps*.1) #LowPAss Filtere - how much I trust my old number and how much I trust the reading to have trend it has to sum 1
    fps1=(str(fpsFilter)+' fps')
    ignore, frame = cam.read() #read frame from the webcam 
    frame[140:220,250:390]=(255,0,255) # Method1 to add rectangle in the middle of the frame
    cv2.rectangle(frame,upperLeft,lowerRight,rectColor,lineW) # Add rectagle line and uses the connection of 2 points Upper Left to lower Right as limit for the size, color and thichness, solid box thickness -1
    cv2.circle(frame, (int(width/2),int(height/2)),myRadius,circleColor,circleThickness) #Add Circle the center, the radius, color and thicness, -1 is full color 
    cv2.putText(frame,fps1,(5,20),myFont,1,textColor,2) # create text Fonts, font size scale with 1 being ??? 1, is font height and 2 is font thickness
    cv2.imshow('myWebCam',frame) #sShow Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()