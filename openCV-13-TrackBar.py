import cv2
print (cv2.__version__)

width =1280 #width ideally keep it on standard sizing 640x480 1280x720
height=720 #height ideally keep it on standard sizing 640x480 1280x720
xPos = int (width/2)
yPos = int (height/2)
myRad=25
myThick = 1

def myCallBack1(val): #anytime you move the track bar it passes the etting of the trackbar as VAR
    global xPos
    print('xVal: ',val)
    xPos=val
  
def myCallBack2(val): #anytime you move the track bar it passes the etting of the trackbar as VAR
    global yPos
    print('yVal: ',val)
    yPos=val

def myCallBack3(val): #anytime you move the track bar it passes the etting of the trackbar as VAR
    global myRad
    print('Radius: ',val)
    myRad=val

def myCallBack4(val): #anytime you move the track bar it passes the etting of the trackbar as VAR
    global myThick
    print('Thickness: ',val)
    myThick=val

cam=cv2.VideoCapture(1,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 locl and 1 external  is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.
#Creat a window for TrackBars
cv2.namedWindow('myTrackBars')
cv2.resizeWindow('myTrackBars',350,150) # Size is width, Height!
cv2.moveWindow ('myTrackBars',1280,0)
#TrackBar Low value is always 0, if we put at another value eg 500 the initial position of the tracker will be at that point only
cv2.createTrackbar('xPos', 'myTrackBars',xPos,width, myCallBack1) # myCallback1 function to process the trackbar event on the xPos!
cv2.createTrackbar('yPos', 'myTrackBars',yPos,height, myCallBack2) # myCallback2 function to process the trackbar event on the yPos!
cv2.createTrackbar('Radius', 'myTrackBars',myRad,int(height/2), myCallBack3) # myCallback2 function to process the trackbar event on the yPos!
cv2.createTrackbar('Thick', 'myTrackBars',myThick,25, myCallBack4) # myCallback2 function to process the trackbar event on the yPos!

while True:

    ignore, frame = cam.read() #read frame from the webcam 
    if myThick==25:
        myThick=(-1)

    # Add Circle in the middle of the frame in the x and y pos
    cv2.circle(frame,(xPos,yPos),myRad, (255,0,0),myThick)
       
    cv2.imshow('myWebCam',frame) #Show Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()