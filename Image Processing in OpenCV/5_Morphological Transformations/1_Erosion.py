import cv2 as cv
import numpy as np


img = cv.imread('pictures/morphological.png')
kernel = np.ones((5, 5), np.uint8)  # 5,5 matris kanal yok siyah beyaz
erosion=cv.erode(img,kernel,iterations=1)   # beyaz bolge aşındırma


cv.imshow('orjinal', img)
cv.imshow('erosion', erosion)

cv.waitKey(0)
cv.destroyAllWindows()