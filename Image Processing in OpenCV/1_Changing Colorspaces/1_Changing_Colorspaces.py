import cv2 as cv
import numpy as np


# flags =[i for i in dir(cv) if i.startswith('COLOR_')]
# print(flags)


# to find the HSV value of Green
blue = np.uint8([[[21, 238, 230]]])
hsv_blue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)
print(hsv_blue)
# [H-10, 100,100] and [H+10, 255, 255] 



cap = cv.VideoCapture(0)
while cap.isOpened():

    # Her kareyi alma
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)   # simetri

    # BGR --> HSV dönüstürme
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # HSV'de mavi renk aralığını tanımlama
    lower_blue = np.array([21, 100, 100])
    upper_blue = np.array([41, 255, 255])

    # mavi renkler elde etmek için HSV görüntüsünü eşikleme
    mask_blue = cv.inRange(frame, lower_blue, upper_blue)

    # Bitsel-VE maskesi ve orijinal görüntü
    res_blue = cv.bitwise_and(frame, frame, mask=mask_blue)

    # çıktı
    cv.imshow('frame', frame)
    cv.imshow('mask', mask_blue)
    cv.imshow('res', res_blue)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
