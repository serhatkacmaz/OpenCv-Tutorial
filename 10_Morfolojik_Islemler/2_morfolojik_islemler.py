import cv2
import numpy as np


image = cv2.imread('pictures/morphological.png')
kernel = np.ones((5, 5), np.uint8)  # 5,5 matris kanal yok siyah beyaz

# iterosyanu ne kadar arttırsam o kadar kuvettli yapıyor

# erode işleminden sonra beyaz bölgeyi aşındırmş olduk yani azaldı küçüldü
erosion = cv2.erode(image, kernel, iterations=1)

# dilate işleminden sonra beyaz bölgeyi arrtırmış olduk yani genişletme
dilation = cv2.dilate(erosion, kernel, iterations=1)  # genişletme
#cv2.imshow('erosion', erosion)
#cv2.imshow('dilation', dilation)


# gürültülü resimler
# opening işlemi önce erosion sonrasında dilation işlemi yapar
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# kopuk resimler delikler
# closing işlemi önce dilation işlemi sonrasında erosion işlemi yapar
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


# gradient işlemi dilation - erosion Sonuçta resmin ana hatları görünür
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Top Hat, orjinel - opening(erosion+dilation)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Black Hat, (dilation+erosion)closing - orjinel
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# resmi göster
cv2.imshow('orjinal', image)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('gradient', gradient)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
