import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2
import logging
import time
import os

sio = socketio.Server()

app = Flask(__name__) #'__main__'
speed_limit = 12
model = None

logger = logging.getLogger(__name__)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s | %(filename)s : %(lineno)s] >> %(message)s')


fileHandler = logging.FileHandler(filename="./server.log")

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.setLevel(level=logging.DEBUG)

logger.debug("### Self Driving AI Car SoftWare Started!! ###")

def current_milli_time():
    return round(time.time()*1000)

def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

# @sio.event
# def my_event(data):
#     print('Received data: ', data)

@sio.on('telemetry')
def telemetry(sid, data):
    try:
        speed = float(data['speed'])
        image = Image.open(BytesIO(base64.b64decode(data['image'])))

        filename = str(current_milli_time()) + ".jpeg"
        image.save(os.path.join("logs", filename))
        
        image = np.asarray(image)
        image = img_preprocess(image)
        image = np.array([image])
        steering_angle = float(model.predict(image))
        throttle = 1.0 - speed/speed_limit
        print('{} {} {}'.format(steering_angle, throttle, speed))
        send_control(steering_angle, throttle)
        
        logger.info(f'Driving Data: {round(steering_angle*100)/100} {filename}')
    except:
        logger.warning("Error Occured on receiving data")


@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    logger.debug('Connected to the Socket.')
    
    send_control(0, 0)

def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })

def hello_world(data, da):
    print(data, da)

if __name__ == '__main__':
    model = load_model('model-advance2.h5')
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
    # sio.connect("http://0.0.0.0:4567")