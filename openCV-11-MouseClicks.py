import cv2
print (cv2.__version__)

evt =0
pnt=0

width =640 #width ideally keep it on standard sizing 640x480 1280x720
height=360 #height ideally keep it on standard sizing 640x480 1280x720

def mouseClick(event,xPos,yPos,flags, params): # the event come from seMousecall back send events, Pos, flags and PArams
    global evt # create global variable that can be used by the entire program
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse event was: ', event)
        print('at position: ',xPos,yPos)
        pnt=(xPos,yPos)
        evt =event
    if event==cv2.EVENT_LBUTTONUP:
        print('Mouse event was: ', event)
        print('at position: ',xPos,yPos)
        pnt=(xPos,yPos)
        evt=event
    
    if event== cv2.EVENT_RBUTTONDOWN: # in the case of pushing the button down it will clear the frame as the vent will change value and wone be condisdered in the if statement 
        print('Right Button down: ', event)
        print('at position: ',xPos,yPos)
        pnt=(xPos,yPos)
        evt=event


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set the width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set the height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.
#Creat a window
cv2.namedWindow('myWebCam')
#Add Listent to Moust Click
cv2.setMouseCallback('myWebCam',mouseClick) #if the mouse call back detects an event on the defined wind launch the mouseClick function ...

while True:
    ignore, frame = cam.read() #read frame from the webcam 
    if evt == 1 or evt ==4:
        cv2.circle(frame,pnt, 25, (255,0,0),2)

    cv2.imshow('myWebCam',frame) #Show Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()