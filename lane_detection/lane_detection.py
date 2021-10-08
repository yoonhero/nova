import cv2
import numpy as np
import matplotlib.pyplot as plt


# function: preprocessing the image
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def make_coordinate(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-intercept)/slope)
    x2 = int((y2-intercept)/slope)
    return np.array([x1, y1, x2, y2])


# functino: get the average slope intercept (평균 기울기)
def average_slope_intercept(image, lines):
    try:
        left_fit = []
        right_fit = []
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            intercept = parameters[1]
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
        left_fit_average = np.average(left_fit, axis=0)
        right_fit_average = np.average(right_fit, axis=0)
        left_line = make_coordinate(image, left_fit_average)
        right_line = make_coordinate(image, right_fit_average)
        return np.array([left_line, right_line])
    except:
        return np.array([])


# function: draw line
def display_lines(image, lines):
    try:
        line_image = np.zeros_like(image)
        if lines is not None:
            for x1, y1, x2, y2 in lines:
                cv2.line(line_image, (x1, y1), (x2, y2),  (0, 255, 0), 10)
        return line_image
    except:
        return image

# function: set the interesting region


def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]

    # variable: need to crop polygon shape
    right_point = width // 10
    left_point = width // 10 * 9

    w_point = width // 2
    h_point = height // 2

    polygons = np.array(
        [[(right_point, height), (left_point, height), (w_point, h_point)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


# class: lane detection
class Lane_Detection():
    def detect(self, image):
        lane_image = np.copy(image)
        canny_img = canny(lane_image)
        cropped_image = region_of_interest(canny_img)

        # cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap) → lines
        # image – 8bit, single-channel binary image, canny edge를 선 적용.
        # rho – r 값의 범위 (0 ~ 1 실수)
        # theta – 𝜃 값의 범위(0 ~ 180 정수)
        # threshold – 만나는 점의 기준, 숫자가 작으면 많은 선이 검출되지만 정확도가 떨어지고, 숫자가 크면 정확도가 올라감.
        # minLineLength – 선의 최소 길이. 이 값보다 작으면 reject.
        # maxLineGap – 선과 선사이의 최대 허용간격. 이 값보다 작으며 reject.
        lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180,
                                100, np.array([]), minLineLength=40, maxLineGap=5)

        average_image = average_slope_intercept(lane_image, lines)

        line_image = display_lines(lane_image, average_image)

        # combine the originial image and line_image
        combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
        return combo_image


if __name__ == '__main__':
    image = cv2.imread('road_sample.jpg')

    lane_detection = Lane_Detection()
    result = lane_detection.detect(image)

    cv2.imshow("result", result)
    cv2.waitKey(0)
