import cv2 as cv
import numpy as np


img = cv.imread('pictures/morphological.png')
kernel = np.ones((5, 5), np.uint8)  # 5,5 matris kanal yok siyah beyaz
dilation = cv.dilate(img, kernel, iterations=1)  # beyaz bölge genişletme


cv.imshow('orjinal', img)
cv.imshow('dilation', dilation)

cv.waitKey(0)
cv.destroyAllWindows()
