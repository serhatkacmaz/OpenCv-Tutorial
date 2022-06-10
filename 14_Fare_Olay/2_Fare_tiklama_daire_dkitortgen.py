import numpy as np
import cv2 as cv

drawing = False  # fareye basılırsa True
mode = True  # True ise diktotrgen m tusuna basarsan eğriye geçer.
ix = iy = -1


# diktortgen ve daire cizme
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # left çift tıklanma
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    # mouse hareket ederse
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 255, 0), -1)

    # mouse sol tıkından el kalkarsa
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 255, 0), -1)


# Main
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k==27:
        break

cv.destroyAllWindows()