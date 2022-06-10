import numpy as np
import cv2 as cv

# gri tonlama
img = cv.imread('pictures/messi.png', 0)
rows,cols=img.shape


M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)  # 90 derece döndurma
dst=cv.warpAffine(img,M,(cols,rows))    # konum ayarlama


cv.imshow('orjinal', img)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
