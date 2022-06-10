import cv2
import numpy

# resmin yolu
image_path = 'pictures/adileNasit.jpg'

image = cv2.imread(image_path)  # resmi oku
print('Shape: '+str(image.shape))   # satır,sütun, kanal sayısı


# Aynalanan resim--> top,bottom,left,right,tarz
projected_image = cv2.copyMakeBorder(image, 194, 190, 270, 250, cv2.BORDER_REFLECT)
cv2.imshow('Adile Nasit (Reflect) ', projected_image)  # resmi göster

# Uzatılan resim
extended_image = cv2.copyMakeBorder(image, 100, 200, 300, 400, cv2.BORDER_REPLICATE)
cv2.imshow('Adile Nasit (Replicate)', extended_image)  # resmi göster

# Tekrarlanan resim
repeat_image = cv2.copyMakeBorder(image, 190, 200, 200, 220, cv2.BORDER_WRAP)
cv2.imshow('Adile Nasit (Wrap)', repeat_image)  # resmi göster

# Sarılan resim çerçeve gibi
wrapped_image = cv2.copyMakeBorder(image, 50, 100, 100, 50, cv2.BORDER_CONSTANT, value=(250, 200, 255))
cv2.imshow('Adile Nasit (Constant)', wrapped_image)  # resmi göster


cv2.waitKey(0)
cv2.destroyAllWindows()
