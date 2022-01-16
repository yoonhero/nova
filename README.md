# 자율주행차 AI Automatic Driving Car

<div align="center">
  <img src="https://user-images.githubusercontent.com/57530375/136566049-9c11741c-2e46-464e-862f-721ac7588849.png">
</div>

## 소개

- [초기 완성 자동차 영상](https://www.youtube.com/watch?v=kk2jRKFPXv0)
- [언젠가는 완성 ...]()

![image](https://github.com/yoonhero/OurAICar/blob/master/docs/software_structure.jpg?raw=true)

현재 언론이나 뉴스같은 곳에서도 많이 접할 수 있는 자율주행차를 직접 만들어보고 싶었고 직접 만들기 위해서 친구와 이 프로젝트를 시작하게 되었습니다. 이 프로젝트는 아마도 10월달쯤에 끝날 예정이며 세상을 바꾸기 위한 작은 발걸음이 될 것이라고 생각하고 열심히 노력하고 있습니다.

## Tech Stack

- Tensorflow
- Keras
- Open CV
- YOLO
- RPi.GPIO
- Raspberry Pi

### 이 프로젝트를 진행하기 위해서 배울것

- [x] opencv python
- [x] deeplearning keras
- [x] math

# HardWare Stack

<img src="https://cdn.imweb.me/thumbnail/20201029/d0ea78a892e73.gif" />

언젠가 이렇게 될거...

# SoftWare Stack

## Motor

- [Detail](https://github.com/yoonhero/OurAICar/tree/master/motor)

Raspberry pi 에 모터를 연결해서 돌릴 수 있도록 RPi.GPIO 를 사용하였습니다.
사용하기 쉽도록 하나의 클래스로 만들어서 모터를 편리하게 조절할 수 있도록 하였습니다.

![image](https://blog.kakaocdn.net/dn/8P2FX/btqDx5pALBs/LgjQPsu2XO63Jr95iIRqKk/img.png)

## Object detection

아직 개발중이지만 현재 YOLO 를 이용해서 간단한 물체인식을 구현했지만 속도가 너무 느린 것 같아서 opencv 와 tensorflow 로 다시 제작할 예정입니다.

![image](https://pjreddie.com/media/image/Screen_Shot_2018-03-24_at_10.48.42_PM.png)

YOLO Example

<strong>TO</strong>

![image](https://1.bp.blogspot.com/-HKhrGghm3Z4/Xwd6oWNmCnI/AAAAAAAADRQ/Hff-ZgjSDvo7op7aUtdN--WSuMohSMn-gCLcBGAsYHQ/s1600/tensorflow2objectdetection.png)

Tensorflow Example

## Line Detection

- [Detail](https://github.com/yoonhero/OurAICar/tree/master/lane_detection)

![image](https://github.com/yoonhero/OurAICar/blob/master/docs/line_detection.png?raw=true)

Youtube 및 여러 사이트를 참고해서 OpenCV 로 도로의 선을 추출하는 모듈을 만들었습니다.

<strong>예상 완성 모습!!</strong>

![image](https://i.ytimg.com/vi/G2VaJvNNp4k/hqdefault.jpg)

## Live Streaming

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

- HTTP Request 에 대한 정보(Method, URL, Data, ...)
- Callback 함수

## To be Later

- [ ] Live Streaming
- [ ] Motor Right/Left Turn
- [ ] Lane Detection Algorithm to turn right or left
- [ ] OpenCV Speed Up
- [ ] Object Detection Fastly
- [ ] Live Streaming
- [ ] Connect with Hardware
- [ ] Test And Edit Values
- [ ] Publishing
