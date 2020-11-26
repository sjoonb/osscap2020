import time
import keyboard

while True:

    now=time.localtime()
    print('%02d:%02d:%02d'%(now.tm_hour,now.tm_min,now.tm_sec))
    time.sleep(1)
