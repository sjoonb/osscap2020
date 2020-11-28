from gtts import gTTS
import os

def play_tts(string):
    tts = gTTS(text = string, lang = 'en')
    tts.save("test.mp3")
    os.system("omxplayer test.mp3")
