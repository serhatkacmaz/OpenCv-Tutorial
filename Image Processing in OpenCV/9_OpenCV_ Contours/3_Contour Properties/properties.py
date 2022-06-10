import numpy as np
import cv2 as cv


img = cv.imread('pictures/star.png', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)    # simple eşik uygulama
contours, hierarchy = cv.findContours(thresh, 1, 2)  # kontor tespit etme

# Moment
cnt = contours[0]
M = cv.moments(cnt)

# 1. Aspect Ratio
# Nesnenin sınırlayıcı doğrusunun genişliğinin yüksekliğine oranıdır.
x, y, w, h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h

# 2. Extent
# kontur alanının sınırlayıcı dikdörtgen alanına oranıdır.
area = cv.contourArea(cnt)  # kontor alanı
x, y, w, h = cv.boundingRect(cnt)  # sınırlayıcı alan
rect_area = w*h
extent = float(area)/rect_area

# 3. Solidity
# kontur alanının dışbükey gövde alanına oranıdır.
area=cv.contourArea(cnt)
hull=cv.convexHull(cnt)
hull_area=cv.contourArea(hull)
solidity=float(area)/hull_area

# 4. Equivalent Diameter
# Eşdeğer Çap, alanı kontur alanıyla aynı olan dairenin çapıdır.
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

# 5. Orientation
# Oryantasyon, nesnenin yönlendirildiği açıdır
(x,y),(MA,ma),angle = cv.fitEllipse(cnt)

# 6. Mask and Pixel Points
# Bazen, nesneyi oluşturan tüm noktalara ihtiyacımız olabilir.
# Satır = y ve sütun = x

imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
mask = np.zeros(imgray.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv.findNonZero(mask)
# Numpy koordinatları **(satır, sütun)** biçiminde verirken, OpenCV koordinatları **(x,y)** biçiminde verir


# 7. Maximum Value, Minimum Value and their locations
# Bu parametreleri bir maske görüntüsü kullanarak bulabiliriz.
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray,mask = mask)


# 8. Mean Color or Mean Intensity
mean_val = cv.mean(imgray,mask=mask)

# 9. Extreme Points
# Uç Noktalar, nesnenin en üst, en alt, en sağ ve en sol noktaları anlamına gelir.
# kırmızı nokta
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
