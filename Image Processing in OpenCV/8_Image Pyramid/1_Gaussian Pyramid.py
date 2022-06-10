import cv2 as cv
import numpy as np


img = cv.imread('pictures/messi.png')

lower_reso=cv.pyrDown(img)  # piramittde yukarda
higher_reso=cv.pyrUp(img)   # piramittde aşagıda
higher_reso2 = cv.pyrUp(lower_reso) #  high_reso2,high_reso'ya eşit değildir, çünkü çözünürlüğü bir kez düşürdüğünüzde bilgiyi kaybedersin. 

# çıktı
cv.imshow('Orjinal',img)
cv.imshow('lower_reso',lower_reso)
cv.imshow('higher_reso',higher_reso)
cv.imshow('higher_reso2',higher_reso2)
cv.waitKey(0)
cv.destroyAllWindows()