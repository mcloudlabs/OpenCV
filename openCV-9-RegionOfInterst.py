import cv2
print (cv2.__version__)

width =640 #width ideally keep it on standard sizing 640x480 1280x720
height=360 #height ideally keep it on standard sizing 640x480 1280x720

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order /Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.

while True:
    ignore, frame = cam.read() #read frame from the webcam 
    frameROI=frame[150:210,250:390] #define the Region of Interest
    frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY) # this will conver the image into matrix of single values as it is GrayScale
    frameROIBGR=cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR) # put the image in BGR MAtrix with tuple of 3 (B,G,R) with the same value keeping the orignal image GRay
    frame[0:60,0:140]=frameROI
    frame[150:210,250:390]=frameROIBGR
    
    cv2.imshow('windowROI',frameROI)
    cv2.imshow('windowROIGray',frameROIGray)
    cv2.imshow('windowROIBGR',frameROIBGR)
    cv2.imshow('myWebCam',frame) #sShow Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    cv2.moveWindow('windowROI',650,0) # Position the window 650 pixel from top left
    cv2.moveWindow('windowROIGray',650,90) # Position the window 650 pixel from top left with 90 pixel down from top
    cv2.moveWindow('windowROIBGR',650,180) # Position the window 650 pixel from top left with 180 pixel down
                         
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()