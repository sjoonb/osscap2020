import pygame, pygcurse
from pygame.locals import *
#rom matrix import *
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

def numberIcon(num):
    num=int(num)
    for i in range(0,9):
        if num==i:
            return icons.num_i
        else:
            return 0

iScreen = [[0 for x in range(32)] for y in range(16)]
iScreenDy=16
iScreenDx=32
oScreen=copy.deepcopy(iScreen)

def consoleMatrix(screen):
    for i in screen:
        print(i)

def drawChar(char, screen, width, height, direction, color):
    for i in range(width):
        for j in range(height):
            if char[j][i] == 1:
                screen[direction[1]+j][direction[0]+i] = color


# - Draw Matrix
consoleMatrix(oScreen)
#drawMatrix(oScreen)



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
        temp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
        weather = soup.find('ul', class_="info_list").find('p', class_="cast_txt").text.split(',')[0]

        win.fill('@', fgcolor='black', bgcolor='black')

        print(weather)
        print(temp,"℃")        



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
#        if int(temp) <= 0:
#            TempColor = 'blue' 
#        elif int(temp) > 32:
#            TempColor = 'red'
#        else:
#            TempColor = 'white'

#       # Set Temperatuer Position
#        post1=(1,17)
#        post2=(1,20)
#        post3=(1,23)
#        post4=(1,27)

#       # Draw Temperature
#        if temp<-10:
#            drawChar(icons.Minus, oScreen,3,5,post1,TempColor)
#            drawChar(numberIcon(temp[1]),oScreen,3,5,post2,TempColor)
#            drawChar(numberIcon(temp[2]),oScreen,3,5,post3,TempColor)
#            drawChar(icons.Cdegree,oScreen,4,5,post4,TempColor)
#        if temp<0:
#            drawChar(icons.Minus, oScreen,3,5,post2,TempColor)
#            drawChar(numberIcon(temp[1]),oScreen,3,5,post3,TempColor)
#            drawChar(icons.Cdegree,oScreen,4,5,post4,TempColor)
#        if 0<=temp<10:
#            drawChar(numberIcon(temp[0]),oScreen,3,5,post2,TempColor)
#            drawChar(icons.Cdegree,oScreen,4,5,post3,TempColor)
#
#        if 10<=temp:
#            drawChar(numberIcon(temp[0]),oScreen,3,5,post2,TempColor)
#            drawChar(numberIcon(temp[1]),oScreen,3,5,post3,TempColor)
#            drawChar(icons.Cdegree,oScreen,4,5,post4,TempColor)

    except:
        pass 

def pygcurseMatrix(screen):
    for i in range(16):
        for j in range(32):
            if screen[i][j] == 1:
                win.putchar('@', j, i, 'white')
            elif screen[i][j] == 2:
                win.putchar('@', j, i, 'green')
    win.update()

#def drawMatrix(array):
# color = 0 : 'None', 1 : 'Red', 2 : 'Green', 3 : 'Yellow', 4 : 'Blue', 5 : 'Purple', 6 : 'Crystal', 7 : 'White'
#    for x in range(len(array[0])):
#        for y in range(len(array)):
#            if array[y][x] == 0:
#                LD.set_pixel(x, y, 0)
#            elif array[y][x] == 1:
#                LD.set_pixel(x, y, 4)
#            elif array[y][x] == 2:
#                LD.set_pixel(x, y, 6)
#            elif array[y][x] == 3:
#                LD.set_pixel(x, y, 5)
#            elif array[y][x] == 4:
#                LD.set_pixel(x, y, 7)
#            else:
#                continue

def clock():
    while True:
        now=time.localtime()
        print('%02d:%02d:%02d'%(now.tm_hour,now.tm_min,now.tm_sec))

        #Set Time number position
#        post5=(9,17)
#        post6=(9,20)
#        post7=(9,24)
#        post8=(9,27)

        #hour=str(now.tm_hour)
        #minute=str(now.tm_min)
        #second=str(now.tm_sec)
#        if (hour<10):
            #drawChar(icons.num_0,oScreen,3,5,post5,white)
            #drawChar(numberIcon(hour),oScreen,3,5,post6,white)
#        elif (hour>10):
            #drawChar(numberIcon(hour[0]),oScreen,3,5,post5,white)
            #drawChar(numberIcon(hour[1]),oScreen,3,5,post6,white)
        
#        if (now.tm_min<10):
            #drawChar(icons.num_0,oScreen,3,5,post7,white)
            #drawChar(numberIcon(minute),oScreen,3,5,post8,white)
#        elif (now.tm_min>10):
            #drawChar(numberIcon(minute[0]),oScreen,3,5,post7,white)
            #drawChar(numberIcon(minute[1]),oScreen,3,5,post8,white)
        
        time.sleep(1)

weather()
clock()
schedule.every(10).minutes.do(weather)
schedule.every(1).second.do(clock)


while True:
    schedule.run_pending()
