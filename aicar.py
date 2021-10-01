import matplotlib.pylab as plt
import cv2
import numpy as np
import math

cap = cv2.VideoCapture(1)
YOLO_net = cv2.dnn.readNet("yolov2.weights", "yolo2.cfg")

# YOLO NETWORK 재구성
classes = []
with open("yolo2.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = YOLO_net.getLayerNames()
output_layers = [
    layer_names[i[0] - 1] for i in YOLO_net.getUnconnectedOutLayers()
]


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def mediumVal(spot):
    result = []

    for i in range(4):
        spots = []
        for line in spot:
            spots.append(line[i])
        array = np.array(spots)
        if math.isnan(array.mean()):
            return True
        else:
            result.append(int(array.mean()))
    return result


def draw_the_lines(img, lines, width):
    if type(lines) == 'NoneType':
        return img
    img = np.copy(img)

    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    left_spot = []
    right_spot = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 < width / 2:
                left_spot.append((x1, y1, x2, y2))
            else:
                right_spot.append((x1, y1, x2, y2))

    left_line = mediumVal(left_spot)
    right_line = mediumVal(right_spot)
    slope = []
    if left_line != True:
        x1, y1, x2, y2 = left_line
        if x2 - x1 != 0:

            slope.append((y2 - y1) / (x2 - x1))

        cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)
    if right_line != True:
        x1, y1, x2, y2 = right_line
        if x2 - x1 != 0:

            slope.append((y2 - y1) / (x2 - x1))

        cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)
    text = "Go Straight"

    if slope[0] > 0:
        text = "Right"
    elif slope[0] < 0:
        text = "Left"
    org = (50, 100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, org, font, 1, (255, 255, 0), 2)
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)

    return img


# = cv2.imread('road.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def process(image):
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [(0, height), (0, height / 2),
                                   (width, height / 2), (width, height)]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 50, 150)
    cropped_image = region_of_interest(
        canny_image,
        np.array([region_of_interest_vertices], np.int32),
    )
    lines = cv2.HoughLinesP(
        cropped_image,
        #smaller rho/theta=more accurate longer processing time
        rho=6,  #number of pixels
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25)
    if type(lines) == "NoneType" or lines is None:
        return image
    image_with_lines = draw_the_lines(image, lines, width)

    return image_with_lines


while True:
    # 웹캠 프레임

    ret, frame = cap.read()
    h, w, c = frame.shape
    if ret:
        frame = process(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    # YOLO 입력
    blob = cv2.dnn.blobFromImage(frame,
                                 0.00392, (416, 416), (0, 0, 0),
                                 True,
                                 crop=False)
    YOLO_net.setInput(blob)
    outs = YOLO_net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:

        for detection in out:

            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # 검출 신뢰도
            if confidence > 0.5:
                # Object detected
                # 검출기의 경계상자 좌표는 0 ~ 1로 정규화되어있으므로 다시 전처리
                center_x = int(detection[0] * w)
                center_y = int(detection[1] * h)
                dw = int(detection[2] * w)
                dh = int(detection[3] * h)
                # Rectangle coordinate
                x = int(center_x - dw / 2)
                y = int(center_y - dh / 2)
                boxes.append([x, y, dw, dh])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                print("stop")

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            score = confidences[i]

            # 경계상자와 클래스 정보 투영
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
    cv2.imshow("YOLOv2", frame)
    # 100ms 마다 영상 갱신
    if cv2.waitKey(100) > 0:
        break

cap.release()
cv2.destroyAllWindows()
