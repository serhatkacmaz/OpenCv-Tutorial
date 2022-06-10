import cv2
import numpy

# resmin yolu
image_path = 'pictures/23Nisan.jpg'

image = cv2.imread(image_path)  # resmi oku
print('Shape: '+str(image.shape))   # satır,sütun, kanal sayısı

# 0-> Blue,  1-> Green,  2-> Red

# :,:, tüm piksellerdeki

# image[:, :, 0] = 154    # resmin Blue degerini 154 yap
# cv2.imshow('23 Nisan Blue', image)  # resmi göster

# image[:, :, 1] = 228    # resmin Green degerini 228 yap
# cv2.imshow('23 Nisan Blue Green', image)  # resmi göster

image[:, :, 2] = 130  # resmin Red değerini 130 yap
cv2.imshow('23 Nisan Red Green', image)  # resmi göster

image[10:100, 0:100] = (0, 225, 210)  # [0,225,210]
cv2.imshow('23 Nisan ', image)  # resmi göster

cv2.waitKey(0)
cv2.destroyAllWindows()
