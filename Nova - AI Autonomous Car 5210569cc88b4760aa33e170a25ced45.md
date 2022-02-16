# Nova - AI Autonomous Car

Technical Leap! 🚀

[https://github.com/yoonhero/OurAICar](https://github.com/yoonhero/OurAICar)

## **Instroduction**

Making something by myself is my favorite hobby. I want to use my technological skills to make the most profound task for the engineer. It is Autonomous Self Driving Car. This project will have started in 2021 March. For time to time, I am learning many tech skills like React, Next. And I came back to finish this project. I am looking forward to using this car in the real road someday. This car's name Nova. This means New!!

[Project Gallery](https://www.notion.so/Project-Gallery-7a9eb7c239804751b3fc392df3a06596)

---

![- Sketch -](Nova%20-%20AI%20Autonomous%20Car%205210569cc88b4760aa33e170a25ced45/software_structure.jpg)

- Sketch -

## **Project Steps**

> Maybe finish in this Winter...
> 

**[Beta ver 1.0](https://www.youtube.com/watch?v=kk2jRKFPXv0)**

- Hardware
    - [x]  Simple Car Model
    - [x]  Set Various Arduino Sensor
    - [x]  Steering System with Motor
- Software
    - Arduino
        - [x]  Motor Control with Arduino
        - [x]  Bluetooth Car Control
    - Python
        - [x]  Simple Lane Detection
        - [x]  Simple Yolov2 Object Detection
        - [x]  GPIO Motor Control
        

**Beta ver 2.0**

I’m planning to make LEVEL 3 AI.

- [x]  RaspberryPi Ultrasonic Sensor and LED
- [x]  Live Streaming
- [ ]  Sensor Socket Server (Almost Done)
- [ ]  Object Detection Fastly with Yolov5
- [ ]  Lane Detection To Visualize User GUI
- [ ]  Steering CNN AI
- [ ]  Image Processing Optimization
- [ ]  Test with Simulation
- [ ]  Publishing

**Beta ver 3.0**

It will operate with LEVEL 4 AI.

- Hardware
    - [ ]  Car Advanced Steering System
    - [ ]  And Various Updates…
- Software
    - [ ]  AI Optimize to Raspberry pi
    - [ ]  Car Advanced Control
    - [ ]  Test
    - [ ]  Publishing

## SoftWare Stack

### Autonomous Car Simulation

![https://github.com/yoonhero/OurAICar/blob/master/docs/simulation_structure.jpg?raw=true](https://github.com/yoonhero/OurAICar/blob/master/docs/simulation_structure.jpg?raw=true)

image

### [Carla](https://carla.org/)

CARLA is an open-source simulator for autonomous driving research. CARLA has been developed from the ground up to support development, training, and validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely. The simulation platform supports flexible specification of sensor suites and environmental conditions.

```
.\CarlaUE4.exe -carla-port=2000
```

**[Example - Tesla Autopilot Simulation](https://www.youtube.com/watch?v=6hkiTejoyms)**

### Motor

Raspberry pi 에 모터를 연결해서 돌릴 수 있도록 RPi.GPIO 를 사용하였습니다. 사용하기 쉽도록 하나의 클래스로 만들어서 모터를 편리하게 조절할 수 있도록 하였습니다.

I am using RPi.GPIO to manipulate microservice in Raspberry PI. I make a motor control Class to use it easily.

![https://blog.kakaocdn.net/dn/8P2FX/btqDx5pALBs/LgjQPsu2XO63Jr95iIRqKk/img.png](https://blog.kakaocdn.net/dn/8P2FX/btqDx5pALBs/LgjQPsu2XO63Jr95iIRqKk/img.png)

### Object detection

Using Yolov5, object detection speed is absolutely fast. And this is really real time. It was trained with around 20000 pictures with labelling Car, Pedestrian, Truck, Traffic Light.

![objectdetection.PNG](Nova%20-%20AI%20Autonomous%20Car%205210569cc88b4760aa33e170a25ced45/objectdetection.png)

### Line Detection

Youtube 및 여러 사이트를 참고해서 OpenCV 로 도로의 선을 추출하는 모듈을 만들었습니다.

![https://github.com/yoonhero/OurAICar/blob/master/docs/line_detection.png?raw=true](https://github.com/yoonhero/OurAICar/blob/master/docs/line_detection.png?raw=true)

![https://i.ytimg.com/vi/G2VaJvNNp4k/hqdefault.jpg](https://i.ytimg.com/vi/G2VaJvNNp4k/hqdefault.jpg)

### Live Streaming

비디오를 클라이언트측에서 클라우드 서로 전송하여서 이를 처리한후 클라우드에서 자율주행차에 명령을 내리는 구조로 제작하였습니다.

![https://github.com/yoonhero/OurAICar/blob/master/docs/liveStreaming.jpg?raw=true](https://github.com/yoonhero/OurAICar/blob/master/docs/liveStreaming.jpg?raw=true)

### Socket IO

**Basic Server Setting**

```python
import socketio

# create a Socket.IO server
sio = socketio.Server()

# wrap with a WSGI application
app = socketio.WSGIApp(sio)
```

**Event**

```python
@sio.on('my custom event')
def another_event(sid, data):    
		pass
```

**WSGI**(Web Server Gateway Interface)

Callable Object 라는 녀석을 통해 Web Server 가 요청에 대한 정보를 Application 에 전달한다.

- HTTP Request 에 대한 정보(Method, URL, Data, …)
- Callback 함수

# Contribute

Please contact yoonhero06@naver.com to make this project together.

# License

[MIT License](https://github.com/yoonhero/OurAICar/blob/master/LICENSE.md)