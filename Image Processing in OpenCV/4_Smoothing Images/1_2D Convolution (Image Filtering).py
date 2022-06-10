import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('pictures/messi.png')

# 5*5 kernel
kernel = np.ones((5,5),np.float32)/25   # kernel oluşturma
dst = cv.filter2D(img,-1,kernel)    # averaging filtreleme


# çıktı
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()