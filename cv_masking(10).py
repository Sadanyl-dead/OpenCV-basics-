import cv2 as cv
import numpy as np

img=cv.imread('temp_images/500.jpg')
cv.imshow('Stock',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank image",blank)

#mask circle
mask=cv.circle(blank,(img. shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

#Masked image

masked_image=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image',masked_image)

cv.waitKey(0)