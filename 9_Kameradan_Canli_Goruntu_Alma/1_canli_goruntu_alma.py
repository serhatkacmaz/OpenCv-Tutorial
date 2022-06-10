import cv2
import numpy as np

# parametre olarak 0 yazarsan pc kamerası,
# 1 yazarsan, usb ile takılı olan kamerayı alır
# 2 yazarsan, bir videodan gelen görüntüleri almak için,yada video adresini yazarakda olabilir.

camera = cv2.VideoCapture(0)    # pc kamerası

# ret kameranın çalışıp çalışmadığını kontrol etme
while True:
    ret, frame = camera.read()  # canlı kameradan gelen kamerayı oku,    görüntüyü oku

    frame = cv2.flip(frame,1)  # y eksenine göre yansıt (aynada gördügün gibi)
    cv2.imshow('Canli Yayin', frame)    # framei göster

    # gelen görüntüyü gri yap
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gri', gray_frame)

    # 30 milisaniyede bir ve cıkış q'ya eşit ise, döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()    # kamerayı serbest bırak, videoyla işim bitti

cv2.destroyAllWindows()
