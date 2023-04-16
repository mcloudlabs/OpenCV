import cv2
print (cv2.__version__)

initialSize= 300
xMaxSize = width =1280 #width ideally keep it on standard sizing 640x480 1280x720
yMaxSize = height=720 #height ideally keep it on standard sizing 640x480 1280x720
xPos =0
yPos =0
xSize=0
ySize=0

def myCallBack1 (val):
    global xPos
    print('xVal: ',val)
    xPos=val
    
def myCallBack2 (val):
    global yPos
    print('yVal: ',val)
    yPos=val

def myCallBack3 (val):
    global xSize
    print('xVal: ',val)
    xSize=int(val)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, xSize) #Set tthe width of the camera
    
def myCallBack4 (val):
    global ySize
    print('yVal: ',val)
    ySize=int(val)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,ySize) #Set tthe height of the camera

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.
cv2.namedWindow('myWebCam')
cv2.namedWindow('trackBars')
cv2.moveWindow('trackBars',width,0) # Position the window on Top Left of the screen
cv2.resizeWindow('trackBars',350,150) # Size is width, Height!
cv2.createTrackbar('winPosX','trackBars',0, xMaxSize, myCallBack1)
cv2.createTrackbar('winPosY','trackBars',0, yMaxSize, myCallBack2)
cv2.createTrackbar('winSizeX','trackBars',width, xMaxSize, myCallBack3)
cv2.createTrackbar('winSizeY','trackBars',height, yMaxSize, myCallBack4)
while True:

      
    ignore, frame = cam.read() #read frame from the webcam 
    cv2.imshow('myWebCam',frame) #sShow Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',xPos,yPos) # Position the window on Top Left of the screen

    #Change the WindowSize better to do it with cam.set _FRAME_ to avoid the pixelization if the initial values are smaller than the one we want !

  

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()