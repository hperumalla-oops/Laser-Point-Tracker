import cv2

pf = cv2.VideoCapture("C:\\Users\\Dell\\Videos\\smol.mp4")
print(pf)

while True:
    ret,frame=pf.read() # returns two values- one is boolean value and the other is image
    frame=cv2.resize(frame,(600,450))
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow(frame)
    cv2.imshow(gray)
    k=cv2.waitKey(25)  #defines the playback time of the video
    if k==ord("f"):
        break

pf.release()
cv2.destroyAllWindows()
