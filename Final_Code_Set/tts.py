from gtts import gTTS
import os
import score_func

def play_tts(string):
    tts = gTTS(text = string, lang = 'ko')
    if os.path.isfile("ttsplay.mp3") == True:
        os.remove("ttsplay.mp3")
    tts.save("ttsplay.mp3")
    os.system("omxplayer ttsplay.mp3")


def tts_score(score, g):
    if g == 'd':
        score_str = "현재 점수는" + str(score) + "점 입니다" 
    elif g == 'b':
        score_str = "현재 점수는" + str(score) + "초 입니다" 
    play_tts(score_str)

def tts_high_score(g):
    if g == 'd':
        game = "dodger"
    elif g == 'b':
        game = "brick"
    score = score_func.get_score(game)[0][1]
    if g == 'd':
        if score[0] == '0' and score[1] == '0':
            score = score[2:]
        elif score[0] == '0' and score[1] != '0':
            score = score[1:]
        score_str = "최고 기록은 " + str(score) + "점 입니다"
    elif g == 'b':
        if score[0] == '0':
            score = score[1:]
        score_str = "최고 기록은 " + str(score) + "초 입니다"
    play_tts(score_str)

def tts_set_high_score():
    set_high_str = "최고 기록을 세웠습니다"
    play_tts(set_high_str)

def tts_clock(h, m):
    clock_str = "현재 시각은 " + str(h) + "시 " + str(m) + "분 입니다"
    play_tts(clock_str)

def tts_play_time(ptime):
    if ptime == 0:
        ptime_str = "방금 게임을 시작했습니다"
    else:
        ptime_str = "게임을 이용한 지 " + str(ptime) + "분 지났습니다"
    play_tts(ptime_str)

def tts_weather(h, m, loc, c1, c2, i):
    h = str(h)
    m = str(m)
    c1 = str(c1)
    c2 = str(c2)
    if int(c1) < 0:
        c1 = c1[1:]
        c1 = "영하 " + c1
    if c2 == "기":
        weather_str = h + "시 " + m + "분 현재 " + loc + " 기온은 " + c1 + "도 입니다 어제와 같습니다"
    elif i == "높아요":
        weather_str = h + "시 " + m + "분 현재 " + loc + " 기온은 " + c1 + "도 입니다 어제보다 " + c2 + "도 높습니다"
    elif i == "낮아요":
        weather_str = h + "시 " + m + "분 현재 " + loc + " 기온은 " + c1 + "도 입니다 어제보다 " + c2 + "도 낮습니다"
    play_tts(weather_str)
