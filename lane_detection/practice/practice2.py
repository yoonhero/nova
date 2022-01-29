# from picamera.array import PiRGBArray
# from picamera import PiCamera
# import RPi.GPIO as GPIO
from time import sleep
import numpy as np
import cv2


# camera = PiCamera()
# camera.resolution = (640,480)
# camera.framerate = 20
# rawCapture = PiRGBArray(camera, size=(640, 480))
# sleep(0.1)

# def make_coordinate(img, line_parameters):
#     print(line_parameters)
#     slope, intercept = line_parameters
#     y1 = img.shape[0]
#     y2 = int(y1 * (3/5))
#     x1 = int((y1-intercept)/slope)
#     x2 = int((y2-intercept)/slope)
#     return np.array([x1,y1,x2,y2])


# def average_slope_intercept(img, lines):
#     left_fit = []
#     right_fit = []
#     for line in lines:
#         x1,y1,x2,y2 = line.reshape(4)
#         parameters = np.polyfit((x1, x2), (y1, y2), 1)
#         slope = parameters[0]
#         intercept = parameters[1]
#         if slope < 0:
#             left_fit.append((slope, intercept))
#         else:
#             right_fit.append((slope, intercept))
#     left_fit_average = np.average(left_fit, axis=0)
#     right_fit_average = np.average(right_fit, axis=0)
#     left_line = make_coordinate(img, left_fit_average)
#     right_line = make_coordinate(img, right_fit_average)
#     return np.array([left_line, right_line])


# def region_of_interest(img, vertices):
#     mask = np.zeros_like(img)
#     match_mask_color = 255
#     cv2.fillPoly(mask, vertices, match_mask_color)
#     masked_image = cv2.bitwise_and(img, mask)
#     return masked_image

# def draw_the_lines(img, lines):
#     img=np.copy(img)
#     print(lines, img)
#     blank_img = np.zeros((img.shape[0], img.shape[1],3), dtype=np.uint8)
#     print(blank_img)
#     for line in lines:
#         print(line)
#         x1,y1,x2,y2 = line
#         cv2.line(blank_img, (x1,y1), (x2,y2),(0,255,0), thickness=4)
#     img = cv2.addWeighted(img, 0.8, blank_img, 1,0.0)
#     return img

# def process(img):
#     height = img.shape[0]
#     width = img.shape[1]
#     region_of_interest_vertices = [
#         (0, height),
#         (0, height/2),
#         (width, height/2),
#         (width, height)
#     ]
#     gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#     gray_img= cv2.GaussianBlur(gray_img, (5,5), 0)
#     canny_image = cv2.Canny(gray_img, 50, 150)
#     cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32),)
#     lines = cv2.HoughLinesP(cropped_image, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)
#     averaged_lines = average_slope_intercept(img, lines)
#     image_w_lines = draw_the_lines(img, averaged_lines)
#     return image_w_lines


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:

            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0),
                     thickness=10)
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)

    return img


# = cv2.imread('road.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def process(image):
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [(0, height), (width / 2, height / 2),
                                   (width, height)]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(
        canny_image,
        np.array([region_of_interest_vertices], np.int32),
    )
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180,
                            100, np.array([]), minLineLength=40, maxLineGap=5)
    image_with_lines = draw_the_lines(image, lines)

    return image_with_lines

# camera.start_preview()

# for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
#     image = frame.array
#     # image = process(image)'
#     image = process(image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     rawCapture.truncate(0)


cap = cv2.VideoCapture("../test/lane_detection_3.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
# camera.stop_preview()
cv2.destroyAllWindows()
# camera.close()
