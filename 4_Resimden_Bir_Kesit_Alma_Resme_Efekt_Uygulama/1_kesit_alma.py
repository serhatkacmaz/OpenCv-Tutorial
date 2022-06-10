import cv2
import numpy as np

# resmin yolu
image_path = 'pictures/23Nisan.jpg'

image = cv2.imread(image_path)  # resmi oku
print('Orjinal Shape: '+str(image.shape))   # satır,sütun, kanal sayısı


section = image[0:100, 250:380]  # 0-99 satır 250-379 sutun aradaki kesit al

# Alınan kesit ile koyulan kısım aralıgı aynı miktarda olmalıdır.
image[0:100, 0:130] = section   # resmin içine kesiti koy, 
print('Alıntı Shape:'+str(section.shape))


cv2.imshow('23 Nisan Resim', image)  # resmi göster
cv2.imshow('Kesit Resim', section)  # kesiti göster

cv2.waitKey(0)
cv2.destroyAllWindows()
