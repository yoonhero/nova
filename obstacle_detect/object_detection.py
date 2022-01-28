from matplotlib import pyplot as plt
import io
from PIL import Image
import cv2
import torch
import os

model = torch.hub.load("ultralytics/yolov5", "custom", path="./best.pt")

def get_prediction(img_bytes,model):
    img = img_bytes
    # inference
    results = model(img, size=640)  
    
    return results


cap = cv2.VideoCapture("./driving_video/driving3.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
            img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (560, 860))

            results = get_prediction(img, model)
            results.render()

            processed_img = cv2.cvtColor(results.imgs[0], cv2.COLOR_BGR2RGB)
            
                    
            # print(results.xyxy[0])  # img1 predictions (tensor)
            print(results.pandas().xyxy[0])  # img1 predictions (pandas)
                    
            # # compute difference
            # difference = cv2.subtract(img, processed_img)

            #         # color the mask red
            # Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
            # ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
            # difference[mask != 255] = [0, 0, 255]

            
            cv2.imshow('Result', processed_img)
            # cv2.imshow('Diff', difference)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()