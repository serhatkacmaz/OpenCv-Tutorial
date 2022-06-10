import cv2
import numpy as np

# Otsu thresholding, değer seçme zorunlulluğunu kaldırır.
# otsu yöntemi kendisi otomatik olarak belirliyor (eşik)

image = cv2.imread('pictures/labirent.png', 0)

# simple thresholding
ret1, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
print(ret1)

# otsu thresholding
# eşik değeri vermiyoruz, BGR sınır değerini veriyoruz min,max olarak
ret2, thresh2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(ret2)


# resmi göster
cv2.imshow('orjinal', image)
cv2.imshow('simple', thresh1)
cv2.imshow('otsu', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
