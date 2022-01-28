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

img = cv2.imread("test.jpg",cv2.COLOR_BGR2RGB)


processed_img = get_prediction(img, model)
# # RGB_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
# im_arr = cv2.imencode('.jpg', processed_img)[1]

# cv2.imwrite('result.jpg', im_arr)
processed_img.render()


RGB_img = cv2.cvtColor(processed_img.imgs[0], cv2.COLOR_BGR2RGB)
# im_arr = cv2.imencode('.jpg', RGB_img)[1]

cv2.imwrite('result.jpg', RGB_img)    

# plt.imshow(RGB_img)
# plt.title('Image')
# plt.show()

cv2.imshow('Result', RGB_img)
cv2.waitKey()