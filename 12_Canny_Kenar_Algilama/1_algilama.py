import cv2
import numpy as np

image = cv2.imread('pictures/groot.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # gri yapma

# küçük küçük istemediğim kenarlar olabilir, engellemek için blur işlemi yumuşatma gibi (gürültü azaltma)
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# alt, üst eşik değerleri
edges = cv2.Canny(blur_image, 70, 100)

cv2.imshow('Orjinal',image)
cv2.imshow('Kenar', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
