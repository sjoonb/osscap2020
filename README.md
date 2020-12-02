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
- 1번 부터 14번까지만 진행 (15번 부터는 윈도우 용)    
    
이후 terminal 창에 입력 ([FILE_NAME] 은 본인이 다운로드한 .json 파일의 이름을 입력해야 한다)      
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
</code>
</pre>
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

## 날씨 및 게임 플레이

Final_Code_Set 으로 이동

소스코드 실행
<pre>
<code>
$ python3 main.py
</code>
</pre>

오류 없이 실행이 된다면 음성 인식이 시작되고 음성을 통하여 기능을 선택한다.    
음성 인식 및 출력은 한국어로 이루어진다.
각 기능에서 선택할 수 있는 기능을 블럭으로 구분하였다.

메인  
> 날씨 - 날씨 모듈을 실행한다    
>> 날씨 - 한번더 '날씨' 음성 입력시, 크롤링을 통한 음성출력이 이루어진다  
>>> 뒤로 - 날씨 모듈이 종료된다        
>>
>> 뒤로 - 메인으로 이동한다  
>
> 게임 - 게임 선택이 가능해 진다     
>> 피하기 - 피하기 게임을 실행한다 
>>> 키보드     
>>> 마우스     
>>> 센서     
>>>> 게임 모드 선택 후, v 키를 입력하여 음성인식이 시작된다   
>>>>> 점수 - 현재 진행중인 게임의 점수가 음성으로 출력된다     
>>>>> 최고 기록 - 현재 진행중인 게임의 최고 기록이 음성으로 출력된다      
>>>>> 플레이 시간 - 메인에서 게임 선택 후 지금까지의 게임 플레이 시간이 음성으로 출력된다      
>>
>> 벽돌 - 벽돌 게임을 실행한다   
>>> 키보드     
>>> 마우스     
>>> 센서    
>>>> 게임 모드 선택 후, v 키를 입력하여 음성인식이 시작된다   
>>>>> 점수 - 현재 진행중인 게임의 점수가 음성으로 출력된다     
>>>>> 최고 기록 - 현재 진행중인 게임의 최고 기록이 음성으로 출력된다      
>>>>> 플레이 시간 - 메인에서 게임 선택 후 지금까지의 게임 플레이 시간이 음성으로 출력된다      
>>
>> 플레이 시간 - 게임 선택 후 지금까지의 게임시간을 출력한다        
>>
>> 뒤로 - 메인으로 이동한다   

