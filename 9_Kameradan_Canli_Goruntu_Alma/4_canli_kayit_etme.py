import cv2

cap = cv2.VideoCapture(0)

#  çerçevenin genişligini al
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

#  çerçevenin yüksekliğini al
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# genişlik - height
print(width, height)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # format mp4
# 3. parametre ile video hızını belirliyoruz (video hızı) ms cinsinden
writer = cv2.VideoWriter('videos/Canli_Kayit.mp4', fourcc, 10, (width, height))

while True:
    ret, frame = cap.read()

    if ret is not True:
        print('Görüntü Okunmadı.')

    frame = cv2.flip(frame, 1)  # y simetri
    
    writer.write(frame)  # frame' i yaz

    cv2.imshow('Kayit Videosu', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()   # serbsest bırak
writer.release()    # serbest bırak
cv2.destroyAllWindows()
