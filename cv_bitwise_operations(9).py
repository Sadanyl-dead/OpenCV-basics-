import cv2 as cv
import numpy as np 

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#Bitwise AND - берет 2 изображдения , накладывает друг на друга и  возваращает пересечение 

bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise and',bitwise_and)

#Bitwise OR  - берёт 2 изображения  , находит пересечения , и те что не пресекаются , и соединяет их вместе 
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwise_or)

#Bitwise XOR - находит не пересекающиеся области 
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bitwise_xor)

#Bitwise NOT - инвертирует изображение (тоесть меняет цвет фигуры с белого на чёрный в данном случае) 
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('Rectangle Bitwise NOT',bitwise_not)

cv.waitKey(0)