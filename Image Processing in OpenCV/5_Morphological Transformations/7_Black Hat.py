import cv2 as cv
import numpy as np


img = cv.imread('pictures/morphological.png')
kernel = np.ones((5, 5), np.uint8)  # 5,5 matris kanal yok siyah beyaz
tophat  = cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)  # closing - input image


cv.imshow('orjinal', img)
cv.imshow('tophat', tophat)

cv.waitKey(0)
cv.destroyAllWindows()
