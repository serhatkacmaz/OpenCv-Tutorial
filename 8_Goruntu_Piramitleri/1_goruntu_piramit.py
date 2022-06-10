import cv2
import numpy


image_path = 'pictures/nataliePortman.jpg'
image = cv2.imread(image_path)  # resmi oku
print('Orjinal Shape: '+str(image.shape))   # satır,sütun, kanal sayısı


# cv2.pyrUp() metodu ile resmin satır sütün degerini iki ile çarpar.
twofold = cv2.pyrUp(image)
print('iki kati Shape: '+str(twofold.shape))   # satır,sütun, kanal sayısı


# cv2.pyDown() metodu ile resmin satır sütün degerini iki ile böler.
half_size = cv2.pyrDown(image)
print('Yarısı Shape: '+str(half_size.shape))   # satır,sütun, kanal sayısı


# resmi göster
cv2.imshow('Portre Orjinel', image)
cv2.imshow('Portre 2X', twofold)
cv2.imshow('Porte Yarı Boyut ', half_size)


cv2.waitKey(0)
cv2.destroyAllWindows()
