import cv2 as cv
import numpy as np


img = cv.imread('pictures/morphological.png')
kernel = np.ones((5, 5), np.uint8)  # 5,5 matris kanal yok siyah beyaz
gradient =cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)   # dilation - erosion


cv.imshow('orjinal', img)
cv.imshow('gradient', gradient)

cv.waitKey(0)
cv.destroyAllWindows()