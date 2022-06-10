import cv2
import numpy as np

# birden fazla görüntüyü göstermek için
from matplotlib import pyplot as plt

# simple thresholding, burda her piksel için aynı eşik değeri uygulanır.
# piksel değeri eşikten küçük ise sıfıra ayarlanır.

image = cv2.imread('pictures/labirent.png',0)


# 2.parametre eşik, piksel piksel bakarak 127 nin altında olanlar sıfıra yuvarlanır (0 olur)
# 3.parametre , eşik değeri üstünde olursa olucağı değer
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# kullanılan eşik değeri, çıktı yani görüntü 2 değer döner (simple thresholding)
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)    # THRESH_BINARY tersidir
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

# görüntüleri tek karede göster
titles = ['Original Image', 'BINARY','BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)    # 2 satır, 3 sütun
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])    # resimlere başlik
    plt.xticks([])  # x noktası değerleri boşalt
    plt.yticks([])  # y noktası değerleri boşalt

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
