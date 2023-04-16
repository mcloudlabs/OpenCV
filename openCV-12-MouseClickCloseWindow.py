import cv2
print (cv2.__version__)

evt =0
pnt1=0
pnt2=0

rectColor=(0,255,0)
lineW=4

width =640 #width ideally keep it on standard sizing 640x480 1280x720
height=360 #height ideally keep it on standard sizing 640x480 1280x720

def mouseClick(event,xPos,yPos,flags, params): # the event come from seMousecall back send events, Pos, flags and PArams
    global evt # create global variable that can be used by the entire program
    global pnt1 # point where the mouse is pressed 
    global pnt2 # point where the mouse is released! 
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse event was: ', event)
        print('at position: ',xPos,yPos)
        pnt1=(xPos,yPos)
        evt =event
    if event==cv2.EVENT_LBUTTONUP:
        print('Mouse event was: ', event)
        print('at position: ',xPos,yPos)
        pnt2=(xPos,yPos)
        evt=event
    
    if event== cv2.EVENT_RBUTTONUP: # in the case of pushing the button down it will clear the frame as the vent will change value and wone be condisdered in the if statement 
        print('Right Button down: ', event)
        print('at position: ',xPos,yPos)
        pnt=(xPos,yPos)
        evt=event

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.

#Creat a window with no picture
cv2.namedWindow('myWebCam')
#Add Listent to Moust Click
cv2.setMouseCallback('myWebCam',mouseClick) #if the mouse call back detects an event on the defined wind launch the mouseClick function ...

while True:
    ignore, frame = cam.read() #read frame from the webcam 
   
    if evt == 4:
        cv2.rectangle(frame,pnt1,pnt2,rectColor,lineW) # Add rectagle line and uses the connection of 2 points Upper Left to lower Right as limit for the size, color and thichness, solid box thickness -1
        ROI = frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
        cv2.imshow('myROI',ROI)
        cv2.moveWindow('myROI', int(width+20),0)
    if evt == 5:
        cv2.destroyWindow ('myROI') # Close window
        evt=0

    cv2.imshow('myWebCam',frame) #sShow Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()