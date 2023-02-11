import cv2

cap = cv2.VideoCapture("MyVideo.mp4")

while True:
    success, frame = cap.read()
    cv2.imshow("Output", frame)
    if cv2.waitKey(30) & 0xFF ==ord('q'):
        break