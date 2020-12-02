## 20년도 2학기 오픈소스기초설계 프로젝트

#### 실행 방법

## 깃 클론
<pre>
<code>
$ git clone https://github.com/sjoonb/osscap2020.git
</code>
</pre>

## 마이크 설정 
참고:  <http://diy-project.tistory.com/88>   

## pyaudio 설치
참고:  <http://diy-project.tistory.com/91>   
<pre>
<code>
$ sudo apt-get update
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo apt-get install python-dev
$ sudo pip install pyaudio
</code>
</pre>

## stt 설치
참고:  https://webnautes.tistory.com/1247   
- 1번 부터 14번까지만 진행 (15번 부터는 윈도우 용도)    
    
이후 terminal 창에 입력
<pre>
<code>
$ export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
</code>
</pre>
requirements.txt 가 있는 폴더로 이동
<pre>
<code>
$ cd /home/pi/osscap2020/stt/microphone
</code>
</pre>
이후 다음 명령어 실행
<pre>
<code>
$ pip3 install -r requirements.txt
</code>
</pre>

### stt 설치 오류 시

- cloud.google.com/docs/authentication/getting-started 링크가 뜨며 실행이 안될 시
<pre>
<code>
$ export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
</pre>
</code>
- stt [Errno -9999] Unanticipated host error     
라즈베리파이 오른쪽 위에 볼륨 아이콘 우클릭하여 사용할 마이크, 스피커 장비 직접 선택해줘야함

## Final_Code_Set 라이브러리 설치

<pre>
<code>
pip3 install gtts
pip3 install pygcurse
pip3 install urlib.request
pip3 install bs4
pip3 install urlib
pip3 install requests
pip3 install pygame
pip3 install RPi.GPIO
pip3 install 
</code>
</pre>
이 외에도 module 이 없다는 오류가 있을시
<pre>
<code>
$ pip3 install (modulename)
</code>
</pre>
