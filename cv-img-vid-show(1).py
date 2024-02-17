import cv2 as cv
import pyautogui

vid = cv.VideoCapture(1)

cv.namedWindow('FS', cv.WINDOW_NORMAL)  # Создаем окно с возможностью изменения размера
pyautogui.hotkey('alt', 'space', 'n')  # Минимизируем окно с помощью pyautogui
#rescale img , videos , and live videos
def rescale(frame,scale=0.5):
    weight=int(frame.shape[0]*scale)
    height=int(frame.shape[1]*scale)
    dimension = (weight,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
#change res Live video 
def changeres(width,height) : 
    vid.set(10,width)
    vid.set(4,height)


while True:
    isTrue, frame = vid.read()
    final=rescale(frame)
    cv.imshow('FS', final)


    if cv.waitKey(20) & 0xFF == ord('d'):  # Для выхода при нажатии 'd'
        break

cv.destroyAllWindows()  # Закрываем все окна OpenCV
