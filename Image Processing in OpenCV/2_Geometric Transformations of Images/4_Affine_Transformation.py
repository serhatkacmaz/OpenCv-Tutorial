import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pictures/drawing.png')
rows, cols, ch = img.shape

# 2*2 matris green noktalar
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[100, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows))

# çıktı
plt.subplot(121),plt.imshow(img),plt.title('orjinal')
plt.subplot(122),plt.imshow(dst),plt.title('dst')
plt.show()