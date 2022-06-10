import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Histogram eşitleme, görüntünün histogramı belirli bir bölgeyle sınırlandırıldığında iyidir

img = cv.imread('pictures/tsukuba_l.png', 0)
equ = cv.equalizeHist(img,) # equalization
res = np.hstack((img, equ))  # yan yana iki resim
cv.imwrite('pictures/tsukuba_l22.png', res)
