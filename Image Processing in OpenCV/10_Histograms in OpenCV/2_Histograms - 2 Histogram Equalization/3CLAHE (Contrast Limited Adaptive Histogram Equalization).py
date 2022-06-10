import numpy as np
import cv2 as cv
img = cv.imread('pictures/tsukuba_l.png',0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv.imwrite('pictures/clahe_2.jpg',cl1)