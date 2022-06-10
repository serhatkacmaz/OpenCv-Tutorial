import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# resim ile template
img_rgb = cv.imread('pictures/mario.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('pictures/mario_template.png', 0)  # mario parası
print('template shape:'+str(template.shape))
w, h = template.shape[::-1]


# Birden çok oluşumu olan bir nesne aradığınızı varsayalım, cv.minMaxLoc() size tüm konumları vermeyecektir.
# Bu durumda, eşikleme kullanacağız
res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
print('Loc: '+str(loc))

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), 255, 2)


plt.subplot(121), plt.imshow(res)
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_rgb,)
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
