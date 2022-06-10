import cv2 as cv
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(x+y)  # 4

img1 = cv.imread('pictures/aslan.jpg')
img2 = cv.imread('pictures/fil.jpg')

# fil resmi üzerinde boyutunu aslanın boyutuna eşitledim yoksa add işleminde hata olurdu
img2 = img2[0:648, 0:1024]
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)


cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
