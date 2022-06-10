import numpy as np
import cv2 as cv
img = cv.imread('pictures/messi.png')


# yeniden boyutlandırma x ve y noktasına göre x' 2kat genişlet
res = cv.resize(img, None, fx=2, fy=1, interpolation=cv.INTER_LINEAR)

cv.imshow('Orjinal', img)
cv.imshow('res -> Fx,Fy', res)

# OR

height, width = img.shape[:2]  # satır,sütün al
res = cv.resize(img, (1*width, 2*height), interpolation=cv.INTER_CUBIC)
cv.imshow('res -> height width', res)
cv.waitKey(0)
cv.destroyAllWindows()
