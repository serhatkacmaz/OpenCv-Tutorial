import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pictures/home.jpg', 0)
# img'nin genişlik yüksekliği ile siyah görüntü
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:500, 100:700] = 255  # beyaz deger at seçili piksellere
masked_img=cv.bitwise_and(img,img,mask=mask)

# Histogramı maskeli ve maskesiz hesaplama
hist_full=cv.calcHist([img],[0],None,[256],[0,256]) # full histogram    # Mavi renk
hist_mask=cv.calcHist([img],[0],mask,[256],[0,256]) # maskeleme, bazı bolgeye göre histogram # turuncu

#çıktı
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()