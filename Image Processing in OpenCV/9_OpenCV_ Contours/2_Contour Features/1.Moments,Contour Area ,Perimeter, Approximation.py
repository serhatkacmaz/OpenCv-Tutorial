import numpy as np
import cv2 as cv

img = cv.imread('pictures/star.png', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)    # simple eşik uygulama
contours, hierarchy = cv.findContours(thresh, 1, 2)  # kontor tespit etme

# 1.Moments
cnt = contours[0]
M = cv.moments(cnt)
print(M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


# 2.Contour Area
# cv.contourArea() işlevi tarafından veya M['m00'] anlarından verilir.
area = cv.contourArea(cnt)
print(area)
print(M['m00'])

# 3. Contour Perimeter
perimeter = cv.arcLength(cnt, True)    # 2. arguman kontor kapalı ise Ture olur


# 4. Contour Approximation

epsilon = 0.01*cv.arcLength(cnt, True) # 2. arguman kontor kapalı ise Ture olur
approx=cv.approxPolyDP(cnt,epsilon,True) # 3. arguman eğrinin kapalı olup olmadığını belirtir.

# kontor çizme
cv.drawContours(img,[approx], 0, (150), 3)  


# çıktı
cv.imshow('orjinal', img)
cv.waitKey(0)
cv.destroyAllWindows()
