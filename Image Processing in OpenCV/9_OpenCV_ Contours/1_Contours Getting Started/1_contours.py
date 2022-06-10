import numpy as np
import cv2 as cv

img = cv.imread('pictures/test.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # gri tonlama
ret, thresh = cv.threshold(imgray, 127, 255, 0)  # thresholding

# Contours, görüntüdeki tüm konturların bir Python listesidir.
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE  )

# kontor cizme
cv.drawContours(img, contours, -1, (255, 0, 0), 3)  # 3.arguman tüm contorları cizmek için -1,  4 ve 5 parametre renk kalınlık 


# çıktı
cv.imshow('orjinal', img)
cv.waitKey(0)
cv.destroyAllWindows()
