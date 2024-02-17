import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

# Загрузка изображения
img = cv.imread('temp_images/500.jpg')
cv.imshow('Stock',img)

# Создание черного изображения того же размера, что и исходное, для использования в маске
blank = np.zeros(img.shape[:2], dtype='uint8')

# Создание круглой маски
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

# Применение маски к изображению
mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)

# Построение RGB гистограммы
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])  # Вычисление гистограммы для текущего канала цвета
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

# Код для построения гистограммы оттенков серого, но закомментирован, так как не используется
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
"""

# Ожидание нажатия клавиши для закрытия окон 
cv.waitKey(0)
