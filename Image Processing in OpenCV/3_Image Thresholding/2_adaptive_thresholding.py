import cv2
import numpy as np
from matplotlib import pyplot as plt

# adaptive thresholding, burda her piksel için aynı eşik değeri kullanmak işimize gelmeyebilir.
# resmin etrafında küçük bir bölgeye göre bir pikselin eşiği alınıyor, bölgesellendirme

image = cv2.imread('pictures/sudoku.png', 0)
image=cv2.blur(image,(3,3))

# simple thresholding
ret, thresh1 = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)


# adaptive thresholding, 2.eşik değeri üstünde olursa olucağı değer
# ortalamalarına göre eşik alma
# son iki parametre bölge ayarı
thresh2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


# resmi göster

titles = ['Original Image','Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [image, thresh1, thresh2, thresh3]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
