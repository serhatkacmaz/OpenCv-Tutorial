# OpenCV, iki şekli veya iki konturu karşılaştırmamızı sağlayan ve benzerliği gösteren bir metrik döndüren cv.matchShapes() işleviyle birlikte gelir .
# Sonuç ne kadar düşükse, eşleşme o kadar iyidir. Hu-moment değerlerine göre hesaplanır. Dokümanlarda farklı ölçüm yöntemleri açıklanmıştır.

import cv2 as cv
import numpy as np
img1 = cv.imread('pictures/messi.png',0)
img2 = cv.imread('pictures/messi.png',0)
ret, thresh = cv.threshold(img1, 127, 255,0)
ret, thresh2 = cv.threshold(img2, 127, 255,0)
contours,hierarchy = cv.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv.findContours(thresh2,2,1)
cnt2 = contours[0]
ret = cv.matchShapes(cnt1,cnt2,1,0.0)
print( ret )