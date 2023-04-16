import cv2
print (cv2.__version__)

cam =cv2.VideoCapture(0) #assign a webcam to a variable cam 0 is the usb order

while True:
    ignore, frame = cam.read() #read frame from the webcam 
    cv2.imshow('myWebCam',frame) #sShow Image (frame) that was captured by .read
    cv2.moveWindow('myWebCam',0,0) # Position the window on Top Left of the screen
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()