import cv2
import numpy

# resim aslan
image_lion = cv2.imread('pictures/aslan.jpg')  # resmi oku
print('Lion Shape: '+str(image_lion.shape))   # satır,sütun, kanal sayısı
cv2.imshow('Aslan', image_lion)  # resmi göster

# resim fil
image_elephant = cv2.imread('pictures/fil.jpg')
print('Elephant Shape: '+str(image_elephant.shape))   # satır,sütun, kanal sayısı
cv2.imshow('Fil', image_elephant)  # resmi göster


# BGR Değerleri
print(image_lion[100, 250])
print(image_elephant[300, 400])


# Ağırlıklı toplam  Bir kanal 0-255 arası değer alır 2 kanal toplamı 255'ten büyük ise katlarının üstüne ne kadar eklendiğine bakılır.
print('Ağırlıklı Toplam:', end='')
print(image_lion[100, 250]+image_elephant[300, 400])

cv2.waitKey(0)
cv2.destroyAllWindows()