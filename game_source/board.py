import LED_display as LD
import random
import threading
import keyboard
import time
import os


t = threading.Thread(target=LD.main, args=())
t.setDaemon(True)
t.start()

while(True):
    LD.set_pixel(1, 0, 2)
    #LD.set_pixel(1, 0, 0)
    time.sleep(5)
