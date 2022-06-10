import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('pictures/sudoku.png')
rows,cols,ch = img.shape

# Matris degerler,
pts1 = np.float32([[28,30],[197,27],[12,200],[206,204]]) # 4 köse noktası
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])    # çıktada nereye gelecegi

M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))

# çıktı
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()