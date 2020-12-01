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

<Final_Code_set 파이썬 코드들의 library 설치>
pip3 install gtts



# 설치 오류시
- cloud.google.com/docs/authentication/getting-started 링크가 뜨며 실행이 안될시엔
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"

- stt [Errno -9999] Unanticipated host error
pyaudio 문제일 확률이 높음
- stt [Errno -9999] Unanticipated host error
