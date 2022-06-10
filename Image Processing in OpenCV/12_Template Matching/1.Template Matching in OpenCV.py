import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# resim ve template
img = cv.imread('pictures/messi.png', 0)
img2 = img.copy()
template = cv.imread('pictures/messi_template.png', 0)  # messi kafası
w, h = template.shape[::-1]

# Bir listede karşılaştırma için 6 yöntemin tümü
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    print('method'+str(method))

    # Apply template Matching
    # daha büyük bir görüntüde bir şablon görüntüsünün konumunu aramak ve bulmak için kullanılan bir yöntem.
    res = cv.matchTemplate(img, template,method)

    # Giriş resminin boyutu (GxY) ve şablon resminin boyutu (gxh) ise, çıktı resminin boyutu (G-g+1, Y-h+1) olacaktır.
    # Sonucu aldıktan sonra , maksimum/minimum değerin nerede olduğunu bulmak için cv.minMaxLoc() işlevini kullanabilirsiniz.
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    # Yöntem TM_SQDIFF veya TM_SQDIFF_NORMED ise, minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    print('top_left', str(top_left))
    bottom_right = (top_left[0]+w, top_left[1]+h)
    # sol üst kose ve sag alt kose tespitten sonra
    cv.rectangle(img, top_left, bottom_right, 255, 2)

    # cıktı
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
