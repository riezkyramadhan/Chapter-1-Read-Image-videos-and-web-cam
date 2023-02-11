import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)#widht id no 3
cap.set(4,480)#height id no 4
cap.set(10,100)#brightness id no 10

while True:
    success, webcam = cap.read()
    cv2.imshow("Output", webcam)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break