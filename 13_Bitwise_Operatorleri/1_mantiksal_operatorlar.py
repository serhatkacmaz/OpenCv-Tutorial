import cv2
import numpy as np
from matplotlib import pyplot as plt


image1 = cv2.imread('pictures/daire.png')
image2 = cv2.imread('pictures/siyah_beyaz_kutu.png')

# mantıksal kapılar mantık beyaz
bit_and = cv2.bitwise_and(image1, image2)
bit_or = cv2.bitwise_or(image1, image2)
bit_xor = cv2.bitwise_xor(image1, image2)   # farklı ise 0 1 --> 1 
bit_not1 = cv2.bitwise_not(image1) 
bit_not2 = cv2.bitwise_not(image2)

# resimleri göster
titles = ['resim1', 'resim 2', 'and', 'or', 'xor', 'not 1', 'not 2']
images = [image1, image2, bit_and, bit_or, bit_xor, bit_not1, bit_not2]

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
