import cv2

img = cv2.imread("MyImage.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)