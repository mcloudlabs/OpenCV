import cv2
print (cv2.__version__)

cam =cv2.VideoCapture(0) #assign a webcam to a variable cam 0 is the us order

while True:
    ignore, frame = cam.read() #read frame from the webcam 
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert the color of frame to gray
    cv2.imshow('myWebCam',frame) #sShow Image (frame) that was captured by .read
    cv2.imshow('myWebCam2',grayFrame) #sShow Image cionverted (grayFrame) 
    cv2.imshow('myWebCam3',frame) #sShow Image (frame) that was captured by .read
    cv2.imshow('myWebCam4',grayFrame) #sShow Image cionverted (grayFrame) 
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    cv2.moveWindow('myWebCam2',640,0) # Position the window on Top Left of the screen
    cv2.moveWindow('myWebCam3',0,510) # Position the window on Top Left of the screen
    cv2.moveWindow('myWebCam4',640,510) # Position the window on Top Left of the screen
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()