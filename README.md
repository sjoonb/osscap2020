# osscap2020

20년도 2학기 오픈소스기초설계 프로젝트

순서대로 실행

git clone https://github.com/sjoonb/osscap2020.git

<마이크 설정>
diy-project.tistory.com/88
위 사이트를 참고하여 마이크 설정

<pyaudio 설치>
diy-project.tistory.com/91 참고
$ sudo apt-get update
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo apt-get install python-dev
$ sudo pip install pyaudio

<stt 사용>
https://webnautes.tistory.com/1247
1번 부터 14번까지만 진행 (15번 부터는 윈도우 용)

이후 terminal 창에 입력
$ export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"

requirements.txt 가 있는 폴더로 이동
cd /home/pi/osscap2020/stt/microphone

이후 다음 명령어 실행
pip3 install -r requirements.txt

<Final_Code_set 파이썬 코드들의 사용 library 설치>
pip3 install gtts
pip3 install pygcurse
pip3 install urlib.request
pip3 install bs4
pip3 install urlib
pip3 install requests
pip3 install pygame
pip3 install RPi.GPIO
pip3 install 

이 외에도 module 이 없다는 오류가 있을시, pip3 install (modulename)

이후 Final_Code_set directory 에서
python3 main.py 로 메인 코드 실행

<사용법> # - 해당 README.md 파일을 raw 로 확인하면 indentation 이 적용된다
음성을 통하여 기능을 선택한다
각 기능에서 선택할 수 있는 기능을 인덴테이션을 활용하여 구분하였다

메인
  날씨 - 날씨 모듈이 실행된다
    날씨 - 한번더 '날씨' 음성 입력시, 크롤링을 통한 음성출력이 이루어진다
    뒤로 - 메인으로 이동한다
  게임 - 게임 선택이 가능해 진다
    피하기 - 피하기 게임을 선택한다
      [모드 선택]
      키보드
      마우스
      센서
        [모든 모드 내에서 v키 입력시 음성인식이 시작된다. 이때 세가지 기능을 활용할 수 있다]
        점수 - 사용자의 현재 점수를 음성으로 출력한다
        최고 기록 - 최고 기록을 음성으로 출력한다
        플레이 시간 - 게임 선택 후 지금까지의 게임시간을 출력한다
      뒤로 - 다시 게임 선택창 으로 이동한다
    벽돌
      [모드 선택]
      키보드
      마우스
      센서
        [모든 모드 내에서 v키 입력시 음성인식이 시작된다. 이때 세가지 기능을 활용할 수 있다]
        점수 - 사용자의 현재 점수를 음성으로 출력한다
        최고 기록 - 최고 기록을 음성으로 출력한다
        플레이 시간 - 게임 선택 후 지금까지의 게임시간을 출력한다
      뒤로 - 다시 게임 선택창 으로 이동한다     
    플레이 시간 - 플레이 시간을 출력한다


# 설치 오류시
- cloud.google.com/docs/authentication/getting-started 링크가 뜨며 실행이 안될시엔
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"

- stt [Errno -9999] Unanticipated host error
라즈베리파이 오른쪽 위에 볼륨 아이콘 우클릭하여 사용할 마이크, 스피커 장비 직접 선택해줘야함





