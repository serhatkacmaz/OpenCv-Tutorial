import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

# (x,y) kordinatlar
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 0,180 yarım elips, 0,360 tam elips, 2.arguman merkez noktası, 3.arguman major ve minor uzunlugu 7.arguman renk, 8.  arguman kalınlık
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# çokgen, int32 tipinde olmalıdır çokgen
# 4 köse kordinati
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 3. parametre False ise kapalı olmayan şekil olur
cv.polylines(img, [pts], True, (0, 255, 255),3)

# put Text
font = cv.FONT_HERSHEY_SIMPLEX
img[10,500]=[255,255,255]
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)


cv.imshow("Resim", img)
cv.waitKey(0)
cv.destroyAllWindows()
