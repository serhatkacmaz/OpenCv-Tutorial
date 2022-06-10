import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print('Bulanamadi.')
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow('Video', frame)
    frame_blur = cv2.GaussianBlur(frame, (3, 3), 0)
    edges = cv2.Canny(frame_blur, 70, 100)

    cv2.imshow('Video_kenar', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
