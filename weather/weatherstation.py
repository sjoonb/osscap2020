import pygame, pygcurse
from pygame.locals import *

#import LED_display as LD
#import threading

from urllib.request import urlopen, Request
import urllib
import bs4

import schedule
import time
import requests

import icons
import copy

#t=threading.Thread(target=LD.main, args=())
#t.setDaemon(True)
#t.start()

win = pygcurse.PygcurseWindow(32, 16, fullscreen=False)

def weather():
    #weather data
    try:
        url = 'https://search.naver.com/search.naver?ie=utf8&query='+ urllib.parse.quote('+날씨')
        
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html,'html5lib')
        location= soup.find('div', class_='select_box').find('span', class_='btn_select').text

        #Get Current Conditions
        temp = int(soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text)
        weather = soup.find('ul', class_="info_list").find('p', class_="cast_txt").text.split(',')[0]

        win.fill('@', fgcolor='black', bgcolor='black')

        print(weather)
        print(temp,"℃")        
        print(icons.Sun)
        pygcurseMatrix(icons.Sun)

#        if weather == '맑음':
#            print(icons.Sun)
#            pygcurseMatrix(icons.Sun)
#            drawMatrix(icons.Sun)
#        elif weather == '흐림':
#            print(icons.Foggy)
#            pygcurseMatrix(icons.Foggy)
#            drawMatrix(icons.Foggy)
#        elif weather == '구름 많음':
#            print(icons.Cloudy)
#            pygcurseMatrix(icons.Cloudy)
#            drawMatrix(icons.Cloudy)
#        elif weather == '비':
#            print(icons.Rain)
#            pygcurseMatrix(icons.Rain)
#            drawMatrix(icons.Rain)
#        elif weather == '눈':
#            print("icons.Snow)
#            pygcurseMatrix(icons.Snow)
#            drawMatrix(icons.Snow)


        # Sets Temperature Color
#        if temp <= 0:
#            TempColor = 'blue'
#        elif temp > 32:
#            TempColor = 'red'
#        else:
#            TempColor = 'white'
#
#        if temp<0:
#            draw -
#            draw 1
#            draw c
#
#        if 0<=temp<10:
#            draw 1
#            draw c
#
#        if 10<=temp:
#            draw 1
#            draw 2
#            draw c

    except:
        pass

# 1 sun 

def pygcurseMatrix(screen):
    for i in range(16):
        for j in range(32):
            if screen[i][j] == 1:
                win.putchar('@', j, i, 'white')
            elif screen[i][j] == 2:
                win.putchar('@', j, i, 'green')
    win.update()

#def drawMatrix(array):
#    for x in range(len(array[0])):
#        for y in range(len(array)):
#            if array[y][x] == 0:
#                LD.set_pixel(x, y, 0)
#            elif array[y][x] == 1:
#                LD.set_pixel(x, y, 2)
#            elif array[y][x] == 2:
#                LD.set_pixel(x, y, 7)
#            elif array[y][x] == 3:
#                LD.set_pixel(x, y, 1)
#            else:
#                continue

def clock():
    while True:
        now=time.localtime()
        #print('%02d:%02d:%02d'%(now.tm_hour,now.tm_min,now.tm_sec))
        if (now.tm_hour<10):
            #print 0
            #print num
            #   print(icons.Sun)
            #   pygcurseMatrix(icons.Sun)
            #   drawMatrix(icons.Sun)
        elif (now.tm_hour>10):
            #print num1
            #print num2
        
        if (now.tm_min<10):
            #print 0
            #print num
        elif (now.tm_min>10):
            #print num1
            #print num2
        
        if (now.tm_sec<10):
            #print 0
            #print num
        elif (now.tm_sec>10):
            #print num1
            #print num2

        time.sleep(1)

weather()
clock()
schedule.every(10).minutes.do(weather)
schedule.every(1).second.do(clock)


while True:
    schedule.run_pending()
