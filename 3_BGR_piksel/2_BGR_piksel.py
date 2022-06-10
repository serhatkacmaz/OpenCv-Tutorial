import cv2
import numpy

# resmin yolu
image_path = 'pictures/joker.jpg'

image = cv2.imread(image_path)  # resmi oku


print('Shape: '+str(image.shape))   # satır,sütün,kanal sayısı
# 50,100 noktasındaki piksele yeni BGR değeri at

# satır,sütün
image[50, 100] = [0, 0, 255]

# 50, i noktasındaki değere yeni BGR degeri
for i in range(100):
    image[50, i] = [0, 0, 255]  # (0,0,255)

cv2.imshow('Joker Resim', image)  # resmi göster
cv2.waitKey(0)
cv2.destroyAllWindows()
