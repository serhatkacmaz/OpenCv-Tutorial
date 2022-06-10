import cv2
import numpy

# resmin yolu
image_path = 'pictures/kemalSunal.jpg'

image = cv2.imread(image_path)  # resmi oku
print('Shape: '+str(image.shape))   # satır,sütun, kanal sayısı

# 0-> Blue,  1-> Green,  2-> Red
image[60:80, 140:205, 1] = 200  # gözlerine efekt yapma


cv2.imshow('23 Nisan ', image)  # resmi göster

cv2.waitKey(0)
cv2.destroyAllWindows()
