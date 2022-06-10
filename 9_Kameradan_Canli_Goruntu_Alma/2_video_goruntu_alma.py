import cv2
import numpy as np


# parametre olarak 0 yazarsan pc kamerası,
# 1 yazarsan, usb ile takılı olan kamerayı alır
# 2 yazarsan, bir videodan gelen görüntüleri almak için,yada video adresini yazarakda olabilir.

video = cv2.VideoCapture('videos/animal_video4k.mp4')    # video yolu

# ret kameranın çalışıp çalışmadığını kontrol etme
while True:
    ret, frame = video.read()  # videyo oku, görüntüyü oku

    frame = cv2.flip(frame, 1)  # y eksenine göre yansıt (aynada gördügün gibi)
    cv2.imshow('Video', frame)    # frame'i göster

    # gelen görüntüyü gri yap
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gri', gray_frame)

    # 30 milisaniyede bir ve cıkış q'ya eşit ise, döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()    # videoyu serbest bırak, işim bitti

cv2.destroyAllWindows()
