import numpy as np
import cv2 as cv


img = cv.imread('pictures/yildiz.png')
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 127, 255, 0)    # simple eşik uygulama
contours, hierarchy = cv.findContours(thresh, 2, 1)  # kontor tespit etme
cnt = contours[0]

# Dışbükeylik kusurlarını bulmak için dışbükey gövdeyi bulurken returnPoints = False olmalı
hull = cv.convexHull(cnt, returnPoints=False)
defects=cv.convexityDefects(cnt,hull)

# döner [ start point, end point, farthest point, approximate distance to farthest point ].
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.line(img,start,end,[0,255,0],2)
    cv.circle(img,far,5,[0,0,255],1)


# 2. Point Polygon Test 
# Bu işlev, görüntüdeki bir nokta ile bir kontur arasındaki en kısa mesafeyi bulur.
# Nokta kontur dışındayken negatif, nokta içerideyken pozitif ve nokta kontur üzerindeyse sıfır olan mesafeyi döndürür.
dist = cv.pointPolygonTest(cnt,(50,50),True)



# çıktı
cv.imshow('orjinal', img)
cv.waitKey(0)
cv.destroyAllWindows()
