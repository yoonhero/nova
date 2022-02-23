![logo](https://capsule-render.vercel.app/api?type=waving&color=e5383b&height=300&section=header&text=Nova&fontAlignY=40&fontSize=90&fontColor=d3d3d3&animation=fadeIn&desc=AutonomouseCar&descSize=30&descAlignY=60)

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

Youtube 및 여러 사이트를 참고해서 OpenCV 로 도로의 선을 추출하는 모듈을 만들었습니다.

<strong>예상 완성 모습!!</strong>

![image](https://i.ytimg.com/vi/G2VaJvNNp4k/hqdefault.jpg)

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

<strong>Beta ver 2.0</strong>

I'm planning to make LEVEL 3 AI.

-   [x] RaspberryPi Ultrasonic Sensor and LED
-   [x] Live Streaming
-   [ ] Sensor Socket Server (Almost Done)
-   [x] Object Detection Fastly with Yolov5
-   [ ] Lane Detection To Visualize User GUI
-   [x] Steering CNN AI
-   [ ] SLAM
-   [ ] Image Processing Optimization
-   [ ] Test with Simulation
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
