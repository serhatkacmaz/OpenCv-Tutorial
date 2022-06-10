import cv2 as cv
import numpy as np



# shape -> (yükseklik,genişlik,kanal)
# zeros() -> tüm elemanları sıfır olan matris yapar.
image = np.zeros((300, 300, 3), dtype='uint8')

print(image.shape)  # shape
print(image)    # piksel değerleri

cv.imshow('Zeros', image)   # resmi göster.


cv.waitKey(0)
cv.destroyAllWindows()
