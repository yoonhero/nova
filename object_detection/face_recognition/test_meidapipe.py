import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    image = cv2.imread("test.jpg")

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = face_detection.process(image)

    # Draw face detections of each face.
    if not results.detections:
        print("Not Detected Any Face")

    annotated_image = image.copy()
    for detection in results.detections:
        print('Nose tip:')
        print(mp_face_detection.get_key_point(
            detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
        mp_drawing.draw_detection(annotated_image, detection)

    cv2.imwrite('annotated_image.png', annotated_image)
