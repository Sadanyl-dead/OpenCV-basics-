import cv2 as cv

# Загрузка изображения
img = cv.imread('temp_images/500.jpg')
cv.imshow('Stock', img)

# Преобразование изображения в оттенки серого
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Простая бинаризация с пороговым значением 40
threshold, thresh = cv.threshold(gray, 40, 255, type=cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# Простая бинаризация с инверсией и пороговым значением 40
threshold, thresh_inv = cv.threshold(gray, 40, 255, type=cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Адаптивная бинаризация с использованием среднего значения блока 11x11
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresh', adaptive_thresh)

# Ожидание нажатия клавиши для закрытия окон
cv.waitKey(0)

# Простая бинаризация:

# Применяет глобальный порог к изображению.
# cv.threshold(gray, 40, 255, type=cv.THRESH_BINARY): 
# Здесь 40 - пороговое значение, 255 - максимальное значение пикселя, type=cv.THRESH_BINARY - тип бинаризации (при котором пиксели, превышающие пороговое значение, устанавливаются в максимальное значение, остальные - в ноль).
# Простая бинаризация с инверсией:

# Также применяет глобальный порог к изображению, но инвертирует результат.
# cv.threshold(gray, 40, 255, type=cv.THRESH_BINARY_INV):
#  Здесь 40 - пороговое значение, 255 - максимальное значение пикселя, type=cv.THRESH_BINARY_INV - тип бинаризации с инверсией (при котором пиксели, превышающие пороговое значение, устанавливаются в ноль, остальные - в максимальное значение).
# Адаптивная бинаризация:

# Вычисляет порог для каждого блока изображения на основе локальных характеристик блока.
# cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3): 
# Здесь gray - исходное изображение, 255 - максимальное значение пикселя, cv.ADAPTIVE_THRESH_MEAN_C - метод вычисления порога (по среднему значению блока), cv.THRESH_BINARY_INV - тип бинаризации с инверсией, 11 - размер блока, 3 - константа, вычитаемая из среднего значения.