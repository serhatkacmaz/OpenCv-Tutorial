from typing import Tuple
import numpy as np
import cv2 as cv

img = cv.imread('pictures/sekil1.png',0)
ret, thresh = cv.threshold(img, 127, 255, 0)    # simple eşik uygulama
contours, hierarchy = cv.findContours(thresh, 1, 2)  # kontor tespit etme

# moments
cnt = contours[0]
M = cv.moments(cnt)
print( M )


# Contour Perimeter
# 2. arguman kontor kapalı ise Ture olur
epsilon = 0.01*cv.arcLength(cnt, True)
# 3. arguman eğrinin kapalı olup olmadığını belirtir.
approx = cv.approxPolyDP(cnt, epsilon, True)

# 5. Convex Hull
# hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]])
# points -> içinden geçtiğimiz konturlardır.
# hull -> çıktıdır, normalde bundan kaçınırız.
# clockwise -> True ise, çıkış dışbükey gövdesi saat yönünde yönlendirilir
# returnPoints -> Varsayılan olarak True,gövde noktalarının koordinatlarını döndürür.
# False ise, gövde noktalarına karşılık gelen kontur noktalarının endekslerini döndürür.

# convex hull(kusur) bulmak için false,
hull = cv.convexHull(cnt)


# 6. Checking Convexity
k = cv.isContourConvex(cnt)  # bir eğrinin dışbukey olup olmadığını döner
print(k)


# 7. Bounding Rectangle
# Straight Bounding Rectangle
# top-left kordinat x,y noktası w genislik, h yukseklik
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(10,20),(30,40),[0,255,0],2)

# Rotated Rectangle
rect = cv.minAreaRect(cnt) # döner ( merkez (x,y), (genişlik, yükseklik), dönüş açısı )
box = cv.boxPoints(rect) # 4 nokta doner diktortgen cizmek için
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2) # kontor cizme


# 8. Minimum Enclosing Circle
(x,y),radius = cv.minEnclosingCircle(cnt)   # x,y merkezi ile capı verir 
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)

# 9. Fitting an Ellipse
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,255,0),2)


# 10. Fitting a Line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)


# çıktı
cv.imshow('orjinal', img)
cv.waitKey(0)
cv.destroyAllWindows()
