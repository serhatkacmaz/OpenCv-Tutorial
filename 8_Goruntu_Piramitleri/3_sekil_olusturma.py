import cv2
import numpy as np
from numpy.lib.type_check import imag


image = np.zeros((300, 300, 3), dtype='uint8')

# cizgi ciz, (x,y)
cv2.line(image, (10, 20), (100, 50), [255, 255, 255], 3)  # başlangıç,bitiş

# daire ciz (x,y)
image[100, 150] = (255, 0, 255)
cv2.circle(image, (150, 100), 25, [255, 0, 255], 2)  # merkez, yarıçap

# metin kutusu koyma 3.parametre başlanıç (x,y)
cv2.putText(image, 'Python OpenCv', [0, 200],cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

# dikdörtgen (x,y)
cv2.rectangle(image, (250, 30), (290, 15), [0, 255, 255], 3)

# resmi göster
cv2.imshow('Resim', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
