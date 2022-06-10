import cv2
import numpy as np

# gürültülü resimlerde

image = cv2.imread('pictures/siyah_beyaz.jpg')
kernel = np.ones((5, 5), np.uint8)  # 5,5 matris kanal yok siyah beyaz


# iterosyanu ne kadar arttırsam o kadar kuvettli yapıyor

# erode işleminden sonra beyaz bölgeyi aşındırmş olduk yani azaldı küçüldü
erosion = cv2.erode(image, kernel, iterations=1)

# dilate işleminden sonra beyaz bölgeyi arttırmış olduk yani genişletme
dilation = cv2.dilate(image, kernel, iterations=1)  # genişletme

cv2.imshow('orjinal', image)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()

