import cv2
import numpy

# resmin yolu
image_path = 'pictures/kurt.jpg'

image = cv2.imread(image_path)  # resmi oku
cv2.imshow('Kurt Resim', image)  # resmi göster

# satır, sütun olarak girilen pikselin BGR değeri gelir
print(image[50, 50])
print(image[(50, 50)])

print('Resmin Boyutu: '+str(image.size))
print('Resmin Özellikleri: '+str(image.shape))
print('Resmin Veri Tipi: '+str(image.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()
