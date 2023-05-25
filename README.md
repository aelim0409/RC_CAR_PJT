# RC_CAR_PJT
---
### [ 프로젝트 개요 ]
##### - 고위험군 산업현장 탐사 및 원격 제어 rc car 제작
---
### [ 개발환경 ]
#### 1. 장치
##### - Raspberry pi 4 , MPU-6050 , PI camera

#### 2. 개발 툴
##### - VNC , Pycharm, Mobaxterm

#### 3. 라이브러리 및 프레임워크
##### - OpenCV, QT

#### 4. DB
##### - MySQL, AWS
---
### [ 핵심 기능 ]

#### 1. 모니터링
##### - 주변 환경 실시간 송출
##### - Camera DeLay 최소화를 위한 별도의 Raspberry Pi 4 사용하여 Pi camera 연결
##### - QT 프레임 워크를 이용한 GUI 제작
##### - OpenCV 사용한 카메라 제어

#### 2. 원격주행
##### - 안정적 주행을 위한 속도, 방항 제어
##### - 3단 변속 기능
##### - Thread를 이용한 RC CAR 모터들 제어

#### 3. Handle Control
##### - 가속도 센서를 활용한 방향전환

#### 4. Database
##### - 시간, RC CAR 속도, 핸들 방향 데이터 저장
##### - 안정적인 데이터 송수신을 위한 Thread 사용
----
### [ 시연 영상 ]

##### - RC CAR
[![미리보기](https://img.youtube.com/vi/OywUcQBBKCM/0.jpg)](https://www.youtube.com/watch?v=OywUcQBBKCM)

##### - 사용자

<img src="https://github.com/aelim0409/RC_CAR_PJT/assets/72659915/354b0336-ded2-442c-ae23-ab27ca46ae94" style="height: 300px;">




