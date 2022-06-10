# her piksel değerine basitçe erişmek ve onu değiştirmek çok yavaş olacaktır, Numpy

import cv2 as cv
import numpy as np

# renkli resim okuma
img = cv.imread('pictures/messi.jpg')

# (satır,sütun)
# 100,100 noktasında renk piksel alma
px = img[100, 100]
print('px: ' + str(px))


# mavi pixel değeri alma BGR
blue = img[100, 100, 0]
print('Blue: '+str(blue))

# piksel modifiye etme
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# En iyi pixel alma ve değiştirme
# kırmızı renk pixel alma
print(img.item(10, 10, 2))

# kırmızı pixel deger güncelleme
img.itemset((10, 10, 2), 255)
print(img.item(10, 10, 2))


# görüntü özellikleri
print('shape: '+str(img.shape))
print('size: '+str(img.size))
print('dtype: '+str(img.dtype))


# görüntü kanallarını bölme ve birleştirme
# tüm renk kanallarını bölme
b, g, r = cv.split(img)
# birleştirme
img = cv.merge((b, g, r))

# blue kanalı alma
b = img[:, :, 0]

# kırmızı kanalları sıfır yapma
img[:, :, 2] = 0

# resmi bastırma
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
