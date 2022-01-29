from matplotlib import pyplot as plt
import io
from PIL import Image
import cv2
import torch
import os

def isExistInDf(df, column, label):
    return False if df.loc[df[column] == label].empty else True

def existDf(df, column, label):
    return df.loc[df[column] == label]


class ObjectDetection(object):
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
    
        self.model = torch.hub.load("ultralytics/yolov5", "custom", path="./best.pt")

    def get_prediction(self,img):
        return self.model(img, size=640)
    
    def process_prediction(self, results_pandas):
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
    

    def process(self,frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = self.get_prediction(image)
        results.render()
        
        processed_img = cv2.cvtColor(results.imgs[0], cv2.COLOR_BGR2RGB)

        stop, processed_prediction = self.process_prediction(results.pandas().xyxy[0])

        return processed_img, stop, processed_prediction
    

if __name__ == "__main__":
    WIDTH = 1280
    HEIGHT = 760
    
    cap = cv2.VideoCapture("./driving_video/driving3.mp4")
    object_detection = ObjectDetection(WIDTH, HEIGHT)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (WIDTH, HEIGHT))

            result, stop, prediction = object_detection.process(img)

            if stop:
                print("### PLEASE STOP ###")
            
            cv2.imshow('Result', result)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("### VIDEO IS ENDED ###")

            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


    cap.release()
    cv2.destoryAllWindows()
