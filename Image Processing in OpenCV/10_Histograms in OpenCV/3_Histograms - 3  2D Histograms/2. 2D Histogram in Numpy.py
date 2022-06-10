import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pictures/home.jpg')
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

# İlk argüman H düzlemidir, ikincisi S düzlemidir, üçüncüsü her biri için kutu sayısı ve dördüncüsü onların aralığıdır.
hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])