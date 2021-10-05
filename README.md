CAN WE MEET
=============
딥러닝을 이용한 감정인식 화상 채팅 웹 앱
-------------
# Environment
## 개발환경
* Web Frontend: HTML5, CSS3, JavaScript, jQeury
* Web Backend: Python/Flask
* Database: MySQL
* STT(Speech-to-Text): Web Speech API, Socket IO
* Meeting API: Twilio

## Virtural Environment
* OS: Windows 10
* Python Version: 3.7
* Packages
  * Flask
  * pyngrok
  * twilio
  * gevent-websocket
  * Flask-SocketIO
  * PyAudio
  * Flask-SQLAlchemy
  * mysql-connector-Python

## Server Environment
* OS: Ubuntu18.06(linux)
* SSH Client: PuTTY
* Packages
  * mysql-server
  * Python3
  * dockcer
  * tensorflow
  
## Deep learning Environment
* Model: CNN, Convolutional Neural Network
* Type: Tensorflow SavedModel
* DataSet
  * 제공 데이터: 회의와 무관한 문장을 Happy, Sad, Angry, Neutral 4가지 감정으로 읽은 한국어 음성파일(600개)
  * 자체 데이터: 자체 제작한 회의 스크립트에 맞춰 4가지의 감정으로 분류하여 직접 음성 데이터 생성(약 300개)
* Libraries
  * librosa
  * sklearn
  * keras
  * tensorflow
 
 # Owner
 * 이정음
 * 김혜인
 * 윤소현
 * 최한나
