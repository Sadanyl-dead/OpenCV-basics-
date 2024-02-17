import cv2 as cv

vid=cv.VideoCapture(1)

while True : 
   # _,frame = vid.read()
    _,frame=vid.read()
    img=cv.imread('IMG_2427.jpg')
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('Cam',img)
    cv.imshow('Cam-gray',gray)
    canny=cv.Canny(gray,125,225)
    cv.imshow("Canny",canny)
    #haar cascade - cамый популярный метод для обнаружения лиц , да он используется но в основном для других обьектов 
    haar_cascade=cv.CascadeClassifier('haar_face.xml')

    face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=12)
    """
    Каждая прямоугольная область описывается четырьмя значениями: (x, y, w, h), где:
    x и y представляют координаты верхнего левого угла прямоугольника,
    w и h представляют ширину и высоту прямоугольника соответственно.
    Таким образом, переменная face_rect представляет собой список кортежей,
    где каждый кортеж содержит координаты и размеры прямоугольной области, в которой обнаружено лицо на изображении.

    """
    #cv.imshow('Face rect',face_rect) #wrong
    
    print(f'Found faces {len(face_rect)}')

    for (x,y,w,h) in face_rect : 
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('Detected Face',img)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()