import cv2 as cv 
import matplotlib.pyplot as mp

img= cv.imread('temp_images/1.jpg')
cv.imshow('Stock',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L+a+b

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

"""
#How BGR in normal programs 
mp.imshow(img)
mp.show()
"""
gray_s = cv.imread('temp_images/res.jpg')
gray_y = cv.imread('temp_images/res.jpg', cv.IMREAD_GRAYSCALE)
color_image = cv.applyColorMap(gray_y, cv.COLORMAP_JET)
rgb1= cv.cvtColor(gray_s,cv.COLOR_BGR2GRAY)
cv.imshow('RGB1',rgb1)
cv.imshow('RGB-TO GREEN',color_image)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

cv.waitKey(0)