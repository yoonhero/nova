import cv2
import numpy as np

circles = np.zeros((4, 2), np.int)
counter = 0


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global counter
        if counter >= 4:
            return
        circles[counter] = x, y
        counter += 1


img = cv2.imread("test_img/book.jpeg")

while True:
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32(circles)
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image", imgOutput)

    for x in range(4):
        cv2.circle(img, (circles[x][0], circles[x][1]),
                   10, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image", mousePoints)

    cv2.waitKey(1)
