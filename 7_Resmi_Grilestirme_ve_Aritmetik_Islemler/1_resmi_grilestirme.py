import cv2
import numpy


image_path = 'pictures/nataliePortman.jpg'
image = cv2.imread(image_path)  # resmi oku
print('Orjinal Shape: '+str(image.shape))   # satır,sütun, kanal sayısı
cv2.imshow('Portre Orjinel', image)  # resmi göster


# renklendirme metodu
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('Gri Shape:' + str(gray_image.shape)) # satır,sütun, kanal sayısı
cv2.imshow('Portre Gri', gray_image)  # resmi göster


cv2.waitKey(0)
cv2.destroyAllWindows()