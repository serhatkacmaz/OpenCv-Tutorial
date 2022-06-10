import cv2
import numpy

# resmin yolu
image_path = 'pictures/kus.jpg'

image = cv2.imread(image_path)  # resmi oku
cv2.imshow('Kus Resim', image)  # resmi göster

print(image)    # matris olarak remi göster
print()

print('Boyut: '+str(image.size))    # resmin toplam piksel sayısını verir. (satır,sütün,kanal sayısı carpımı)
print('Data Tipi: '+str(image.dtype))   # resmin veri tipini verir.

# shape ile dönen değerlerin çarpımı size ile dönen piksel sayısını verir.
print('(Satır, Sütun, Kanal): ' + str(image.shape)) # satır,sütün ve renkli ise kanal sayısını tuple olarak döner.


cv2.waitKey(0)
cv2.destroyAllWindows()