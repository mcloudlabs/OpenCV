import cv2
print (cv2.__version__)

width =640 #width ideally keep it on standard sizing 640x480 1280x720
height=360 #height ideally keep it on standard sizing 640x480 1280x720

snipW= 120
snipH= 60
#initial point of the box Center Row and Center Column
boxCR= int(height/2)
boxCC= int(width/2)

#moving the box in each direction by 1 pixel by changing the delta
deltaRow=1
DeltaColumn=1
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.

while True:
    ignore, frame = cam.read() #read frame from the webcam 
    #select the box ROI
    frameROI=frame[int(boxCR-snipH/2):int(boxCR+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]
    #switch frame color to Gray Scale 

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxCR-snipH/2):int(boxCR+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]=frameROI

    #Move the box into two axis by 1 pixel 

    boxCR=boxCR+deltaRow
    boxCC=boxCC+DeltaColumn

    #Conditions: 
    if boxCR-snipH/2<=0 or boxCR+snipH/2>=height:
        deltaRow=deltaRow*(-1)
    
    if boxCC-snipW/2<=0 or boxCC+snipW/2>=width:
        DeltaColumn=DeltaColumn*(-1)

    cv2.imshow('myROI',frameROI)
    cv2.moveWindow('myROI',650,0) # Position the window on Top Left of the screen
    cv2.imshow('myWebCam',frame) #Show Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()