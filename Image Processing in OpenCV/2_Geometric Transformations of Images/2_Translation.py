import numpy as np
import cv2 as cv

# gri tonlama
img = cv.imread('pictures/messi.png', 0)

# satır sütün alma
rows, cols = img.shape

# (x,y)
# (100,50) konumda kaydırma için
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))   # 2.paramtere kaydırma, 3.parametre cıktının boyutu


cv.imshow('orjinal', img)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
