# Method - 1 : Using cv.imshow()
# Gri tonlamalı bir görüntü olacak ve farklı renklerin Ton değerlerini bilmiyorsanız, 
#orada hangi renklerin olduğu hakkında fazla bir fikir vermeyecektir.

# Method - 2 : Using Matplotlib
# ilk bakışta orada hangi rengin olduğu hakkında bir fikir vermez.  matplotlib.pyplot.imshow() işlevini kullanabiliriz. 
#Farklı piksel yoğunluğu hakkında bize çok daha iyi bir fikir verir. Ancak bu aynı zamanda, farklı renklerin Ton değerlerini bilmiyorsanız,

# Method 3 : OpenCV sample style !!



import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pictures/home.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )

plt.imshow(hist,interpolation='nearest')
plt.show()
# X ekseni S değerlerini ve Y ekseni H gösterir.    


