from matplotlib import pyplot as plt
import io
from PIL import Image
import cv2
import torch
import os


WIDTH = 1280
HEIGHT = 760


model = torch.hub.load("ultralytics/yolov5", "custom", path="./best.pt")

def get_prediction(img_bytes,model):
    img = img_bytes
    # inference
    results = model(img, size=640)  
    
    return results

def isExistInDf(df, column, label):
    return False if df.loc[df[column] == label].empty else True

def existDf(df, column, label):
    return df.loc[df[column] == label]

# results_pandas structure
# xmin  ymin  xmax  ymax  confidence  class  name

def process_prediction(results_pandas):

    labels = {"0":"biker", "1":"car", "2":"pedestrian", "3":"trafficLight", "4": "trafficLight-Green", "5":"trafficLight-GreenLeft", "6":"trafficLight-Red", "7":"trafficLight-RedLeft", "8":"trafficLight-Yellow", "9":"trafficLight-YellowLeft", "10":"truck"}
    
    results = {}
    
    confi_condition = results_pandas["confidence"]> 0.4
    
    confi_result = results_pandas[confi_condition]    
    
    for label in labels.values():
        if isExistInDf(confi_result, "name", label):
            try:
                # return with prediction position
                labelDf = existDf(confi_result,"name", label)                            
                
                labelDf_column = ["xmin", 'xmax', 'ymin', 'ymax']

                labelDf = labelDf.loc[:, labelDf_column]

                
                results[label] = labelDf.values.tolist()
            finally:
                pass

    return len(results.keys()) != 0, results

cap = cv2.VideoCapture("./driving_video/driving3.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (WIDTH,HEIGHT))

        results = get_prediction(img, model)
        results.render()

        processed_img = cv2.cvtColor(results.imgs[0], cv2.COLOR_BGR2RGB)
            
        stop, processed_prediction = process_prediction(results.pandas().xyxy[0])            
        
        if stop:
            print("#### PLEASE STOP ####")
        
        cv2.imshow('Result', processed_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('video is ended')

        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


cap.release()
cv2.destroyAllWindows()