import cv2
import numpy

# resmin yolu
image_path = 'pictures/hababamSinifi.jpg'

image = cv2.imread(image_path)  # resmi oku
print('Shape: '+str(image.shape))   # satır,sütun, kanal sayısı

# (x,y)--> (sütün,satır)

image[100, 115] = [0, 0, 255]
image[50, 152] = [0, 0, 255]

# sol_alt (x,y) kordinatı ile sag_ust (x,y) kordinatı girilir
# 4.parametre rectangle rengi, 5. parametre kalem size 
cv2.rectangle(image, (115, 100), (152, 50), [0, 0, 255], 3)


cv2.imshow('Hababam ', image)  # resmi göster


cv2.waitKey(0)
cv2.destroyAllWindows()
