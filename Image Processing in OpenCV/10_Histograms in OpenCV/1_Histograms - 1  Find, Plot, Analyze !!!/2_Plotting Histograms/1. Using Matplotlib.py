import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pictures/home.jpg', 0)
plt.hist(img.ravel(), 256, [0, 256])  # histSize, Range son parametreler
plt.show()


# BGR olarak renkli
img = cv.imread('pictures/home.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256]) # 2.parametre [0] [1] [2] BGR için
    plt.plot(histr, color=col)  # sırasıyla b,g,r
    plt.xlim([0, 256])
plt.show()
