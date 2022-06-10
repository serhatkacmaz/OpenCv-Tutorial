# 2D Histogram in OpenCV

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pictures/home.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])


#  çıktı 
plt.subplot(221), plt.plot(hist)
plt.show();
