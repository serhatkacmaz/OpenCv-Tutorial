import cv2

# pc kamerası
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret is False:
        print('Görüntü Okunmadı.')

    frame = cv2.flip(frame, 1)  # y ekseni simetrisi

    # - 1 ise içini doldurur
    # (x,y) noktası
    cv2.rectangle(frame, (100, 100), (200, 200), (0, 255, 0), 1)    # dikdörtgen
    cv2.line(frame, (100, 100), (200, 200), (0, 0, 255), 3)   # çizgi
    cv2.circle(frame, (200, 200), 20, (255, 0, 0), -1)   # daire
    cv2.putText(frame, 'Live Broadcast', (0, 300), cv2.FONT_HERSHEY_PLAIN,2, (200, 200, 200), 1)    # text kutusu

    cv2.imshow('Canli Yayin', frame)  # resmi göster

    # 1 milisaniye bekle ve çıkış esc(ASCII) ise
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()   # serbest bırak
cv2.destroyAllWindows()