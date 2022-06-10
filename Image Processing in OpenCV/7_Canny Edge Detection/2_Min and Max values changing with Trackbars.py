import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# izleme çubuğu her değiştiğinde çalışcak function(callback function)
def nothing():
    pass


img = cv.imread('pictures/messi.png', 0)
cv.namedWindow('image')

# trackbar create
cv.createTrackbar('Max Value', 'image', 0, 255, nothing)
cv.createTrackbar('Min Value', 'image', 0, 255, nothing)


while True:
    cv.imshow('image - orjinal', img)

    # esc basınca bitir
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # trackbar mevcut kounmlarını alma
    max_value = cv.getTrackbarPos('Max Value', 'image')
    min_value = cv.getTrackbarPos('Min Value', 'image')

    # canyn edge detection
    edges = cv.Canny(img, min_value, max_value)
    cv.imshow('Edges', edges)
