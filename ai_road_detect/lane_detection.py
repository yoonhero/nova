import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    right_point = width // 10
    left_point = width // 10 * 8

    polygons = np.array(
        [[(right_point, height), (left_point, height), (height//5*4, width//2)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask


image = cv2.imread("../test_img/road.jpg")
lane_image = np.copy(image)
canny = canny(lane_image)

# plt.imshow(canny)
# plt.show()

cv2.imshow("canny", region_of_interest(canny))

cv2.waitKey(0)
