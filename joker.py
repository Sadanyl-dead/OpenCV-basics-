import cv2 as cv
import pyautogui as pg
import time

# Получаем размеры экрана
screen_width, screen_height = pg.size()

# Загрузка видеофайла
vid = cv.VideoCapture('video/gus.mp4')

# Получаем размеры кадра видео
_, frame = vid.read()
video_width = frame.shape[1]
video_height = frame.shape[0]

# Рассчитываем количество окон для отображения видео
num_cols = screen_width // video_width
num_rows = screen_height // video_height
total_windows = num_cols * num_rows


# Отображаем видео в нескольких окнах
while True:
    for i in range(total_windows):
        # Считываем следующий кадр из видео
        is_true, frame = vid.read()
        if not is_true:
            break

        # Рассчитываем координаты верхнего левого угла текущего окна
        start_x = (i % num_cols) * video_width
        start_y = (i // num_cols) * video_height
        pg.hotkey('ctrl','m')
        # Устанавливаем размер окна OpenCV в соответствии с размерами видеокадра
        cv.namedWindow(f'Gus_{i}', cv.WINDOW_NORMAL)
        cv.resizeWindow(f'Gus_{i}', video_width, video_height)
        cv.moveWindow(f'Gus_{i}', start_x, start_y)
        cv.imshow(f'Gus_{i}', frame)

        time.sleep(0.009)
        
    # Выход из цикла, если пользователь нажал клавишу 'd'
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Закрываем все окна OpenCV
vid.release()
cv.destroyAllWindows()

# Добавленная строка для ожидания ввода перед завершением программы
#input("Нажмите Enter для завершения программы...")
