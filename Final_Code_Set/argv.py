import sys
import threading
import LED_display as LD

import time
import copy
import os

print('sys.argv =', sys.argv)

game = sys.argv[1]
score = sys.argv[2]


print("Game: ", game)
print("Score: ", score)
