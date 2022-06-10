import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pictures/messi.png', 0)
hist,bins = np.histogram(img.ravel(),256,[0,256])


#  np.bincount() bundan 10 kat hızlıdır
#  OpenCV function bundan 40 kat hızlıdır
