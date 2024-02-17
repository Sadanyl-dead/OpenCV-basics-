import cv2 as cv
import numpy as np 

img=cv.imread('temp_images/1.jpg')


cv.imshow('STOCK',img)

b,g,r = cv.split(img)
cv.imshow('BLue',b)
cv.imshow('Green',r)
cv.imshow('Red',r)

blank=np.zeros(img.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
merge_img=cv.merge([b,g,r])
cv.imshow('BLue1',blue)
cv.imshow('Green1',green)
cv.imshow('Red1',red)
cv.imshow('MERGE',merge_img)

cv.waitKey(0)