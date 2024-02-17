import cv2 as cv
import pyautogui as pg

# Получаем размеры экрана
screen_width, screen_height = pg.size()

# Загрузка видеофайла
vid = cv.VideoCapture('video/tf2g.mp4')

# Получаем размеры кадра видео
_, frame = vid.read()
video_width = frame.shape[1]
video_height = frame.shape[0]

# Определяем размеры окна равными размерам экрана
window_width = screen_width
window_height = screen_height

# Создаем окно OpenCV
cv.namedWindow('Gus', cv.WINDOW_NORMAL)
cv.resizeWindow('Gus', window_width, window_height)

# Отображаем видео в окне
while True:
    # Считываем следующий кадр из видео
    is_true, frame = vid.read()
    if not is_true:
        break

    # Устанавливаем размер окна OpenCV в соответствии с размерами видеокадра
    cv.imshow('Gus', frame)

    # Проверяем, нажата ли клавиша 'q' для выхода
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Закрываем окно OpenCV и освобождаем ресурсы
vid.release()
cv.destroyAllWindows()
