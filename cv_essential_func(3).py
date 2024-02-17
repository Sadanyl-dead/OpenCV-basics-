import cv2 as cv

blank=cv.imread('temp_images/1.jpg')
cv.imshow('Stock',blank)

#Converting to  grayscale
"""
gray=cv.cvtColor(blank,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
"""

#Blurring image 

"""

blur=cv.GaussianBlur(blank,(1,1),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)


#Edge cascade 
canny= cv.Canny(blur, 245,275)
cv.imshow('Edges',canny)

#Finding edges and blurring are a good combination , blurr image can be used to reduce amount of edges
"""
#Dilating the image - spreading borders of the edges
canny= cv.Canny(blank, 245,275)
dilated= cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dialated',dilated)

#Eroding  - erosing edges from operation Dilating
erode=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',erode)

#Resize and Crop  (to crop image on smaller scale - cv.INTER_AREA , to enlarge - INTER_LINEAR  (fastest - low quality) , INTER_CUBIC (slowest - hishest resolution))
resized=cv.resize(blank,(500,500),interpolation=cv.INTER_CUBIC)

cropped=blank[50:200 , 200:400]
cv.imshow('Cropped',cropped)

cv.imshow('Resized',resized)

cv.waitKey(0)