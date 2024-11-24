import cv2

pf = cv2.VideoCapture(0)


#DIVX, XVID, MJPG, X264, WMVI, WMV2
fourcc =cv2.VideoWriter_fourcc(*"XVID")  #initializes format of how the video file is saved
output = cv2.VideoWriter("C:\\Users\\Dell\\Desktop\\FART\\fart8.avi", fourcc, 20.0,(640,480),0) # location the file, format of the file, frame per second, resolution, 0--> if the images passed are grayscale

print(pf)
while pf.isOpened():
    ret,frame=pf.read() # returns two values- one is boolean value and the other is image
    if ret == True:
        #frame=cv2.resize(frame,(600,450))
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(gray)
        if cv2.waitKey(1) & 0xFF ==ord("f"):   #default 0 for image and 1 for video
            break

pf.release()
output.release()
cv2.destroyAllWindows()
  