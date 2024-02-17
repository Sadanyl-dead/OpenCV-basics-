import cv2 as cv
import numpy as np
img=cv.imread('temp_images/1.jpg')

cv.imshow('Blank',img)

#Translation
def translate(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimension)

# -x --> left
# -y --> up
#  x --> right
#  y --> down

translated=translate(img , 100, 100)
cv.imshow("Translated", translated)

#Rotation
def rotate (img,angle ,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint == None :
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension=(width,height)
    return cv.warpAffine(img,rotMat,dimension)

rotated=rotate(img,45)
cv.imshow('Rotated',rotated)

#Resizing
resized=cv.resize(img , (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)



#Flipping 
"""
1 (или любое положительное целое число): Отражение по вертикали (вокруг горизонтальной оси).
0: Отражение по горизонтали (вокруг вертикальной оси).
-1 (обычно используется): Отражение по горизонтали и вертикали одновременно (вокруг обеих осей).
"""
flip=cv.flip(img,-1)
cv.imshow('Flip',flip)

#Cropping
cropped=img[50:200 , 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)