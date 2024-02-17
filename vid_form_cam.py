import cv2 as cv 
import numpy as np 

vid = cv.VideoCapture(0)
while True :
    _,frame= vid.read()
    blank=np.zeros(frame.shape,dtype='uint8') 
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    canny=cv.Canny(gray,275,275)
    contours,hierarchies=cv.findContours(canny,cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
    print(f'{len(contours)} - amount of contours')

    cv.drawContours(frame,contours,-1,(0,0,255),1)
    cv.imshow('Countours',frame)
    #cv.imshow('VID',canny)
    if cv.waitKey(20) & 0xFF == ord('d') : 
        break


cv.destroyAllWindows()