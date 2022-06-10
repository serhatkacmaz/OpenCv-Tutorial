import numpy as np
import cv2 as cv

# 1. parametre uint8 or float32 tipinde resim parentez içinde verilmeli [img]
# 2.parametre parentez içinde verilmeli, gri ton ise [0], Renkli görüntü için sırasıyla mavi, yeşil veya kırmızı kanalın histogramını
# hesaplamak için [0], [1] veya [2]'yi geçebilirsiniz.
# 3. parametre tam görüntünün histogramını bulmak için None verilir.
# belirli bir bölgesinin histogramını bulmak istiyorsanız, bunun için bir maske görüntüsü oluşturmanız ve onu maske olarak vermeniz gerekir
# 4.parametre BIN sayımızı temsil eder. Köşeli parantez içinde verilmesi gerekir. tam ölcek [256]
# 5.parametre bu bizim RANGE'imizdir. Normalde [0,256]'dır.

# gri tonlu resimde tüm histogram bulmak
img = cv.imread('pictures/messi.png', 0)
hist = cv.calcHist([img], [0], None, [256], [0, 256])

