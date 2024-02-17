import cv2 as cv
import numpy as np



img=cv.imread('temp_images/1.jpg')

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

cv.imshow('IMG',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


blur= cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)


"""
cv.RETR_EXTERNAL: Возвращает только внешние контуры, игнорируя внутренние контуры. Контур считается внешним, если он полностью охватывает внутренние контуры.

cv.RETR_TREE: Возвращает все контуры и строит полную иерархию контуров.

cv.RETR_CCOMP: Возвращает все контуры и разбивает их на двухуровневую иерархию. На верхнем уровне находятся внешние контуры, на нижнем уровне - внутренние контуры.

cv.RETR_FLOODFILL: Внутреннее использование OpenCV.

2)


cv.CHAIN_APPROX_SIMPLE: Сжимает все горизонтальные, вертикальные и диагональные сегменты и оставляет только конечные точки. 
Например, линия с пятью точками будет представлена только конечными точками, а остальные точки будут отброшены.

cv.CHAIN_APPROX_TC89_L1 и cv.CHAIN_APPROX_TC89_KCOS: Два дополнительных метода для аппроксимации контуров, которые используют 
алгоритмы Tchebychev и позволяют получить более точные аппроксимации с меньшим количеством точек, чем cv.CHAIN_APPROX_SIMPLE.

Выбор метода аппроксимации контуров зависит от конкретной задачи и требований к точности и эффективности.
 Если вам необходимо сохранить все точки контура, вы можете использовать cv.CHAIN_APPROX_NONE, но помните,
   что это может привести к большому количеству точек и более сложной структуре данных контура.
"""
ret,thresh=cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('Tresh',thresh)
#canny/tresh
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST , cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} - amount of contours')

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Countours',blank)

#Лучше начать с Canny и передавать данные сюда - contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST , cv.CHAIN_APPROX_NONE) 
#cv.drawChessboardCorners - Ищет и отображает углы шахматной доски 
cv.waitKey(0)