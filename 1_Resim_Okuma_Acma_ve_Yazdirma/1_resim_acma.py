import cv2
import numpy as np

image_logo = cv2.imread('pictures/alev.jpg')    # resmi oku
cv2.imshow('Resim', image_logo)     # resmi pencerede göster

# pencere yaratma ve gösterme
cv2.namedWindow('name', cv2.WINDOW_NORMAL)
cv2.imshow('name', image_logo)

# resmin matrisini verir, her bir piksel içinde 3 kanal vardır BGR
print(image_logo)

# Pencere açıldığında pencerenin kapanması için bir tuşa basılmasını bekler
cv2.waitKey(0)

# çarpıya basınca OpenCv ye bağlım tüm kısımları kapat
cv2.destroyAllWindows()