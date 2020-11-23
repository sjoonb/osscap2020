import pygame, pygcurse
from pygame.locals import *

#import LED_display as LD
#import threading

from urllib.request import urlopen, Request
import urllib
import bs4

import pygame, pygcurse
from pygame.locals import *

from PIL import Image
from PIL import ImageDraw
import schedule
import time
import requests

import icons
import copy

#t=threading.Thread(target=LD.main, args=())
#t.setDaemon(True)
#t.start()

#def drawimage(path, x, y):
#    image = Image.open(open(path),'rb').convert('RGB')
#    image.load()
#    matrix.SetImage(image, x, y)

win = pygcurse.PygcurseWindow(32, 16, fullscreen=False)

def job():
    # Clear matrix
    #matrix.Clear()

    # Pull fresh weather data
    try:
        url = 'https://search.naver.com/search.naver?ie=utf8&query='+ urllib.parse.quote('+날씨')
        
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html,'html5lib')
        location= soup.find('div', class_='select_box').find('span', class_='btn_select').text

        #Get Current Conditions
        temp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
        
        weather = soup.find('ul', class_="info_list").find('p', class_="cast_txt").text
        weather = weather.split(',')[0]

#Draw weather icon
#        if weather=='눈':
#            drawimage('weathericons/' + 'snow' + '.png', 9, 1)
#        elif weather=='비':
#            drawimage('weathericons/' + '09d' + '.png', 9, 1)
#        elif weather=='맑음':
#            #drawimage('weathericons/' + '01d' + '.png', 9, 1)
#        elif weather=='흐림':
#            drawimage('weathericons/' + '03d' + '.png', 9, 1)
#        elif weather=='구름많음':
#            drawimage('weathericons/' + '02d' + '.png', 9, 1)

        #Draw temperature
        TempComponents = str(temp)
        TempLength = len(TempComponents)

        win.fill('@', fgcolor='black', bgcolor='black')

        temp=int(temp)
        print(weather)

        if weather == '맑음':
            print(icons.Sun)
            pygcurseMatrix(icons.Sun)
#            drawMatrix(icons.Sun)
        elif weather == '흐림':
            pass

        print(temp,"°C")

        # Sets Temperature Color
#        if temp <= 0:
#            TempColor = 'b'
#        elif temp > 32:
#            TempColor = 'r'
#        else:
#            TempColor = 'w'
#
#        if TempLength == 1:
#            drawimage('numbericons/' + str(TempComponents[0]) + TempColor + '.png', 11, 16)
#            drawimage('numbericons/' + 'F' + TempColor + '.png', 17, 16)
#
#        if TempLength == 2:
#            drawimage('numbericons/' + str(TempComponents[0]) + TempColor + '.png', 7, 16)
#            drawimage('numbericons/' + str(TempComponents[1]) + TempColor + '.png', 13, 16)
#
#            drawimage('numbericons/' + 'F' + TempColor + '.png', 19, 16)
#
#        if TempLength == 3:
#            drawimage('numbericons/' + str(TempComponents[0]) + TempColor + '.png', 5, 16)
#            drawimage('numbericons/' + str(TempComponents[1]) + TempColor + '.png', 9, 16)
#            drawimage('numbericons/' + str(TempComponents[2]) + TempColor + '.png', 15, 16)
#            drawimage('numbericons/' + 'F' + TempColor + '.png', 21, 16)
#
#        print('Current Temp: '+str(temp)+' Icon Code: '+str(icon))

    except requests.exceptions.RequestException as e:
       drawimage('weathericons/' + 'error' + '.png', 9, 1)

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

job()
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
