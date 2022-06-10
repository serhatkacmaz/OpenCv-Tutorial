import cv2 as cv
import numpy as np


img = cv.imread('pictures/morphological.png')
kernel = np.ones((5, 5), np.uint8)  # 5,5 matris kanal yok siyah beyaz
opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)  # gürültü azlatma  erosion-> dilation


cv.imshow('orjinal', img)
cv.imshow('opening', opening)

cv.waitKey(0)
cv.destroyAllWindows()
