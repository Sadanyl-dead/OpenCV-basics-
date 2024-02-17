import cv2 as cv 
import numpy as np 

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

#1 Painting image green 
"""
blank[:]=0,255,0

cv.imshow('Fianl',blank)
"""
#Range painting 
"""
blank[200:300 , 300:400] = 0,0,211
cv.imshow('Portion',blank)
"""
#Draw rectangle
"""
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
"""
#Filling with color thickness=cv.FILLED or thickness=-1 (same result)
"""
#Part with last cordinates can be provided as (blank[0]//2,blank[1]//3) - as width and height

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)
"""
#Draw a circle 
"""
cv.circle(blank,(250,250),40,(0,0,255),thickness=2)
cv.imshow('Circle',blank)
"""
#Draw a line 
"""
cv.line(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('AS',blank)
"""
#Write text on an image 
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,10,255),thickness=3)
cv.imshow('Text',blank)
cv.waitKey(0)