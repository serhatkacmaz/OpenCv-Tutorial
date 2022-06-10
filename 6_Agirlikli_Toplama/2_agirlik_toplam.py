import cv2
import numpy

# resim aslan
image_lion = cv2.imread('pictures/aslan.jpg')  # resmi oku
print('Shape: '+str(image_lion.shape))   # satır,sütun, kanal sayısı

# resim fil
image_elephant = cv2.imread('pictures/fil.jpg')
print('Shape: '+str(image_elephant.shape))   # satır,sütun, kanal sayısı

# fil resmi üzerinde boyutunu aslanın boyutuna eşitledim yoksa add işleminde hata olurdu
image_elephant = image_elephant[0:648, 0:1024]

# cv2.add metodu() ile iki resmi topladık, agırlıklı olarak alpha değerleri 1 iki resminde
total_image = cv2.add(image_elephant, image_lion)
cv2.imshow('(Add) Toplanmis Resimler', total_image)


# cv2.addWeighted() metodu ile iki resmi ağırlıklı olarak toplama
weighted_picking = cv2.addWeighted(image_lion, 0.6, image_elephant, 0.4, 0)
cv2.imshow('(Add Weighted)Agirlikli Toplanmis Resimler', weighted_picking)

cv2.waitKey(0)
cv2.destroyAllWindows()
