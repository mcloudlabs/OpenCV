import cv2
print (cv2.__version__)

rows= int(input('Please enter the number of rows?  '))
columns= int (input('Please enter the number of columns?  '))


width =1080 #width ideally keep it on standard sizing 640x480 1280x720
height=720 #height ideally keep it on standard sizing 640x480 1280x720

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #assign a webcam to a variable cam 0 is the usb order Direct Show

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #Set tthe width of the camera
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) #Set tthe height of the camera
cam.set(cv2.CAP_PROP_FPS, 30) # set the Frames Per Second 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) #Setting the Codec to MJPG.

while True:
    ignore, frame = cam.read() #read frame from the webcam 
    frame=cv2.resize(frame, (int(width/columns), int(height/columns))) #devide by the same variable Columns to have a good ratio! 
    for i in range(0,rows):
        for j in range (0,columns):
            windName='Window'+str(i)+str(j)
            cv2.imshow(windName,frame) #Show Image (frame) that was captured by .read
            cv2.moveWindow(windName,int(width/columns)*j,int(height/columns+30)*i) # Position the window on Top Left of the screen

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()