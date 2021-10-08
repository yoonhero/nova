import cv2
import numpy as np
import time

# returns stop condition True or False


class ObstacleDetect:
    def __init__(self):
        # YOLO 가중치 파일과 CFG 파일 로드
        self.YOLO_net = cv2.dnn.readNet("yolov2.weights", "yolo2.cfg")
        # YOLO NETWORK 재구성
        self.classes = []
        with open("yolo2.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        self.layer_names = self.YOLO_net.getLayerNames()
        self.output_layers = [
            self.layer_names[i[0] - 1] for i in self.YOLO_net.getUnconnectedOutLayers()
        ]
        self.stop = False

    def recognize(self, frame):
        self.stop = False
        h, w, c = frame.shape

        # YOLO 입력
        blob = cv2.dnn.blobFromImage(frame,
                                     0.00392, (416, 416), (0, 0, 0),
                                     True,
                                     crop=False)
        self.YOLO_net.setInput(blob)
        outs = self.YOLO_net.forward(self.output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:

            for detection in out:

                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:
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
                    self.stop = True

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                try:

                    label = str(self.classes[class_ids[i]])
                    score = confidences[i]

                    # 경계상자와 클래스 정보 투영
                    cv2.rectangle(frame, (x, y), (x + w, y + h),
                                  (0, 0, 255), 5)
                    cv2.putText(frame, label, (x, y - 20), cv2.FONT_ITALIC, 0.5,
                                (255, 255, 255), 1)

                except:
                    pass
        cv2.imshow("YOLOv2", frame)

        return self.stop


if __name__ == "__main__":
    obstacle_detect = ObstacleDetect()
    cap = cv2.VideoCapture(1)

    while True:
        # 웹캠 프레임
        ret, frame = cap.read()
        h, w, c = frame.shape
        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

        stop = obstacle_detect.recognize(frame)

        if stop:
            print("stop!!")

    cap.release()
    cv2.destroyAllWindows()
