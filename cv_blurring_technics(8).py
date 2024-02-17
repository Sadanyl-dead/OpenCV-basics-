import cv2 as cv

img=cv.imread('temp_images/500.jpg')
cv.imshow('Stock',img)

#Averaging - считачет  среденее значение  интенсевности пикселей вокруг центра (который мы и меняем)
avg=cv.blur(img,(3,3))
cv.imshow('Avarage Blur',avg)

#Gaussin - даёт пикселям вес и так же расчитывает среденее значение (ядро нечетное (3,3 итд.)) как и Avarage (выглядит более натурально чем предидущий)
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussin Blur',gauss)

#Median Blur  - Тоже что и Avarage , только вместо среднего значения - медиана , лучше убирает шум чем предидущие (не рачитан на большой кол-во шумов (7,7 итд))
median=cv.medianBlur(img,3) # не кортеж в ядре , потому что автоматом считает 3 на 3

cv.imshow('Median Blur',median)

#Bilaterial BLur - самый эффективнй , применяет блюр но оставляет грани 
bilaterial = cv.bilateralFilter(img,10,15,25) # 3 это не мейн ядро сетки , это диаметр соседних пикселей . Две 15 1 - цветовая сигма , отвечает за колво вовлеченных в цветом плане , а 2 - сколько пискелей от центра повлияют на расчёты 
cv.imshow('Bilaterial',bilaterial)

cv.waitKey(0)