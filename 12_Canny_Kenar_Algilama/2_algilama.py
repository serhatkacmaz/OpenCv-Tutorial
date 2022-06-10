import cv2
import numpy as np

from matplotlib import pyplot as plt
from numpy.core.defchararray import title

image = cv2.imread('pictures/groot.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # gri yapma


# küçük küçük istemediğim kenarlar olabilir, engellemek için blur işlemi yumuşatma gibi
blur_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
blur_image = cv2.blur(blur_image, (3, 3))


# otomatik olarak sigma değerine göre eşik değerlerini üret ve kenarları bulan method
def autoCanny(blur, sigma=0.33):
    # görüntüdeki piksel yoğunlukların medyanını hesapla
    median = np.median(blur)
    lower = int(max(0, (1.0-sigma)*median))   # alt eşik değeri
    upper = int(max(255, (1.0-sigma)*median))  # üst eşik değeri
    edges = cv2.Canny(blur, lower, upper)
    return edges


wide = cv2.Canny(blur_image, 10, 220)   # geniş şekilde eşikler
tight = cv2.Canny(blur_image, 200, 230)  # dar şekilde eşikler
auto = autoCanny(blur_image,100)


# yanyana resmi göster
cv2.imshow('Edges: wide tight auto(canny)', np.hstack([wide, tight, auto]))
cv2.imshow('wide', wide)

# resim göster
titles = ['orjinal', 'blurred image', 'canny edge detection']
images = [image, blur_image, auto]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
