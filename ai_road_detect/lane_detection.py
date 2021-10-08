import cv2
import numpy as np

image = cv2.imread("../test_img/road.jpg")
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(gray, 50, 150)

cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("canny", canny)

cv2.waitKey(0)
