import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('pictures/wiki.jpg', 0)

# numpy function ile histogram alma
hist, bin = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')

plt.hist(img.flatten(),256,[0,256], color = 'r')    # histogram cizme plt ile
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left') # gösterge
plt.show()


cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

# yüz tanımada, yüz verilerini eğitmeden önce, yüzlerin görüntüleri, hepsini aynı aydınlatma koşullarında yapmak için histograma eşitlenir.