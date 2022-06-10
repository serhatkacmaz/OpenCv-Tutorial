import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('pictures/messi.png')

# 1. Averaging
blur = cv.blur(img, (5, 5))

# 2. Gaussian Blurring
blur=cv.GaussianBlur(img,(5,5),0)   # gürültü azaltmada iyidir

# 3. Median Blurring
median = cv.medianBlur(img,5)

# 4.Bilateral Filtering
blur=cv.bilateralFilter(img,9,75,75)
# çıktı
plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(median), plt.title('median')
plt.xticks([]), plt.yticks([])
plt.show()
