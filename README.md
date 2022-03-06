![logo](https://capsule-render.vercel.app/api?type=waving&color=e5383b&height=300&section=header&text=Nova&fontAlignY=40&fontSize=90&fontColor=d3d3d3&animation=fadeIn&desc=AutonomouseCar&descSize=30&descAlignY=60)

[![wakatime](https://wakatime.com/badge/user/5f9867f2-894f-4b38-acf8-ebc89cb7f4e6/project/2fbb121c-40e4-4d78-8151-7bb4af59ba32.svg)](https://wakatime.com/badge/user/5f9867f2-894f-4b38-acf8-ebc89cb7f4e6/project/2fbb121c-40e4-4d78-8151-7bb4af59ba32)
[![wakatime](https://wakatime.com/badge/user/5f9867f2-894f-4b38-acf8-ebc89cb7f4e6/project/3addceec-91df-41fd-84dd-2024c24e77ae.svg)](https://wakatime.com/badge/user/5f9867f2-894f-4b38-acf8-ebc89cb7f4e6/project/3addceec-91df-41fd-84dd-2024c24e77ae)

# Instroduction

[Beta Version 1.0 Demo](https://www.youtube.com/watch?v=kk2jRKFPXv0)

이 프로젝트를 완성하는 것이 세상을 바꾸기 위한 작은 발걸음이 될 것이라고 생각하고 열심히 노력하고 있습니다.

Making something by myself is my favorite hobby. I want to use my technological skills to make the most profound task for the engineer. It is Autonomous Self Driving Car. This project will have started in 2021 March. For time to time, I am learning many tech skills like React, Next. And I came back to finish this project. I am looking forward to using this car in the real road someday.

This car's name <strong>["Nova"](https://en.wiktionary.org/wiki/nova)</strong> is named after Esperanto. This means New!

![image](https://github.com/yoonhero/OurAICar/blob/master/docs/software_structure.jpg?raw=true)

## Installation

```bash
git clone https://github.com/yoonhero/OurAICar
```

Cloning my Project...

```bash
pip install -r requirements.txt
```

Please install [Tensorflow](https://github.com/tensorflow/tensorflow) and [Pytorch](https://github.com/pytorch/pytorch) by following steps which introduces those installation guides.

**Conda**

```bash
conda env create -f environment.yml
```

Export Requirements.yml

```bash
conda activate mlenv
conda env export > environment.yml
```

## SoftWare Stack

### Autonomous Car Simulation

![image](https://github.com/yoonhero/OurAICar/blob/master/docs/simulation_structure.jpg?raw=true)

### [Carla](https://carla.org/)

CARLA is an open-source simulator for autonomous driving research. CARLA has been developed from the ground up to support development, training, and validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely. The simulation platform supports flexible specification of sensor suites and environmental conditions.

```
.\CarlaUE4.exe -carla-port=2000
```

<strong>[Example - Tesla Autopilot Simulation](https://www.youtube.com/watch?v=6hkiTejoyms)</strong>

### Motor

Raspberry pi 에 모터를 연결해서 돌릴 수 있도록 RPi.GPIO 를 사용하였습니다.
사용하기 쉽도록 하나의 클래스로 만들어서 모터를 편리하게 조절할 수 있도록 하였습니다.

I am using RPi.GPIO to manipulate microservice in Raspberry PI. I make a motor control Class to use it easily.

![image](https://blog.kakaocdn.net/dn/8P2FX/btqDx5pALBs/LgjQPsu2XO63Jr95iIRqKk/img.png)

### Object detection

Using Yolov5, object detection speed is absolutely fast. And this is really real time. It was trained with around 20000 pictures with labelling Car, Pedestrian, Truck, Traffic Light.

![image](https://github.com/yoonhero/OurAICar/blob/master/docs/objectdetect.PNG?raw=true)

### Line Detection

![image](https://github.com/yoonhero/OurAICar/blob/master/docs/line_detection.png?raw=true)

<strong>Camera Calibration 카메라 교정</strong>

우리가 실제 눈으로 보는 세상은 3차원이지만 이것을 카메라로 찍으면 2차원의 이미지로 변하게 된다. 이때 3차원의 점들이 이미지 상에서 어디에 맺히는지는 기하학적으로 생각하면 영상을 찍을 당시의 카메라의 위치 및 방향에 의해 결정된다. 하지만 실제 이미지는 사용된 렌즈, 렌즈와 이미지 센서와의 거리, 렌즈와 이미지 센서가 이루는 각 등 카메라 내부의 기구적인 부분에 의해서 크게 영향을 받는다. 따라서 3차원 점들이 영상에 투영된 위치를 구하거나 역으로 영상 좌표로부터 3차원 공간좌표를 복원할때에는 이러한 내부 요인을 제거해야만 정확한 계산이 가능해진다. 그리고 이러한 내부 요인의 파라미터 값을 구하는 과정을 카메라 캘리브레이션이라고 부른다.

![calibration](https://github.com/yoonhero/nova/blob/master/docs/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-11-28%2010.57.53.png?raw=true)




Youtube 및 여러 사이트를 참고해서 OpenCV 로 도로의 선을 추출하는 모듈을 만들었습니다.

<strong>예상 완성 모습!!</strong>

![image](https://i.ytimg.com/vi/G2VaJvNNp4k/hqdefault.jpg)

### Kalman Filter

칼만 필터(Kalman filter)는 잡음이 포함되어 있는 측정치를 바탕으로 선형 역학계의 상태를 추정하는 재귀 필터로, 루돌프 칼만이 개발하였다. 칼만 필터는 컴퓨터 비전, 로봇 공학, 레이다 등의 여러 분야에 사용된다. 칼만 필터는 과거에 수행한 측정값을 바탕으로 현재의 상태 변수의 결합분포를 추정한다.

> P*예상값 = P*추정값 - 상수*상수*P*추정값 = (1-상수)\*P*추정값

```python
cv2.KalmanFilter(int dynamParams, int measureParams, int controlParams=0, int type=CV_32F)
```

<strong>Example</strong>

```python
import cv2
import numpy as np

class KalmanFilter:
    kf = cv2.KalmanFilter(4, 2)
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)


    def predict(self, coordX, coordY):
        measured = np.array([[np.float32(coordX)], [np.float32(coordY)]])
        self.kf.correct(measured)
        predicted = self.kf.predict()
        x, y = int(predicted[0]), int(predicted[1])
        return x, y
```

### Live Streaming

![image](https://github.com/yoonhero/OurAICar/blob/master/docs/liveStreaming.jpg?raw=true)

비디오를 클라이언트측에서 클라우드 서로 전송하여서 이를 처리한후 클라우드에서 자율주행차에 명령을 내리는 구조로 제작하였습니다.

### Socket IO

```
pip3 install python-socketio
```

<strong>Basic Server Setting</strong>

```python
import socketio

# create a Socket.IO server
sio = socketio.Server()

# wrap with a WSGI application
app = socketio.WSGIApp(sio)
```

<strong>Event</strong>

```python
@sio.on('my custom event')
def another_event(sid, data):
    pass
```

<strong>WSGI</strong>(Web Server Gateway Interface)

Callable Object 라는 녀석을 통해 Web Server 가 요청에 대한 정보를 Application 에 전달한다.

-   HTTP Request 에 대한 정보(Method, URL, Data, ...)
-   Callback 함수

## Project Steps

<strong>[Beta ver 1.0](https://www.youtube.com/watch?v=kk2jRKFPXv0)</strong>

-   Hardware
    -   [x] Simple Car Model
    -   [x] Set Various Arduino Sensor
    -   [x] Steering System with Motor
-   Software
    -   Arduino
        -   [x] Motor Control with Arduino
        -   [x] Bluetooth Car Control
    -   Python
        -   [x] Simple Lane Detection
        -   [x] Simple Yolov2 Object Detection
        -   [x] GPIO Motor Control

<strong>[Beta ver 2.0](https://www.youtube.com/watch?v=CvH4EfcbqXI)</strong>

I'm planning to make LEVEL 3 AI.

-   [x] RaspberryPi Ultrasonic Sensor and LED
-   [x] Live Streaming
-   [ ] Sensor Socket Server (Almost Done)
-   [x] Object Detection Fastly with Yolov5
-   [ ] Lane Detection To Visualize User GUI
-   [x] Steering CNN AI
-   [ ] SLAM
-   [ ] Image Processing Optimization
-   [x] Test with Simulation
-   [ ] Publishing

<strong>Beta ver 3.0</strong>

It will operate with LEVEL 4 AI.

-   Hardware
    -   [ ] Car Advanced Steering System
    -   [ ] And Various Updates...
-   Software
    -   [ ] AI Optimize to Raspberry pi
    -   [ ] Car Advanced Control
    -   [ ] Test
    -   [ ] Publishing

# Contribute

Please contact yoonhero06@naver.com to make this project together.

# License

[MIT License](https://github.com/yoonhero/OurAICar/blob/master/LICENSE.md)
