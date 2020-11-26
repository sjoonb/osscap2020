import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

trig = 13
echo = 26

print("start")

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.output(trig, gpio.LOW)

def get_distance():
    try :
#        gpio.output(trig, False)

        gpio.output(trig, gpio.HIGH)
        time.sleep(0.00001)
        gpio.output(trig, gpio.LOW)

        while gpio.input(echo) == gpio.LOW :
            pulse_start = time.time()

        while gpio.input(echo) == gpio.HIGH :
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000 * 2
        distance = round(distance)

        print("Distance : ", distance, 'px')

        return distance


    except :
      gpio.cleanup()

if __name__ == '__main__':
    while(True):
        get_distance()
