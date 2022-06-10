# resmi aç gri ton yap ve kaydet

import cv2
import numpy as np

# resmi oku, 0 --> kanalları kapa siyah-beyaz tonda olsun
image_logo = cv2.imread('pictures/alev.jpg', 0)
cv2.imshow('Resim', image_logo)     # resmi pencerede göster

cv2.imwrite('pictures/alev_gri.png', image_logo)    # resmi belirtilen adrese yaz

# Pencere açıldığında pencerenin kapanması için bir tuşa basılmasını bekler
cv2.waitKey(0)

# çarpıya basınca OpenCv ye bağlım tüm kısımları kapat
cv2.destroyAllWindows()
