import cv2 as cv
import numpy as np
from matplotlib import pyplot  as plt

BLUE = [255,0,0]
img1 = cv.imread('pictures/opencv.jpg')


replicate = cv.copyMakeBorder(img1,100,10,10,10,cv.BORDER_REPLICATE)    # uzat
reflect = cv.copyMakeBorder(img1,100,10,10,10,cv.BORDER_REFLECT)    # yansıt
reflect101 = cv.copyMakeBorder(img1,100,10,10,10,cv.BORDER_REFLECT_101)  
wrap = cv.copyMakeBorder(img1,100,10,10,10,cv.BORDER_WRAP)   # sarıcı
constant= cv.copyMakeBorder(img1,100,10,10,10,cv.BORDER_CONSTANT,value=[0,255,0]) # çerçeve


plt.subplot(231),plt.imshow(img1),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()