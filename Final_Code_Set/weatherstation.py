from matrix import *
import LED_display as LD
import threading

from urllib.request import urlopen, Request
import urllib
import bs4
import time
import requests
import copy

import icons

t=threading.Thread(target=LD.main, args=())
t.setDaemon(True)
t.start()


def numberIcon(num):
    iconlist=[number.num_0,number.num_1,number.num_2,number.num_3,number.num_4,number.num_5,number.num_6,number.num_7,number.num_8,number.num_9,number.X]

    for i in range(0,10):
        if int(num)==i:
            return iconlist[i]
    return iconlist[10]

def drawChar(char, screen, width, height, direction, color):
    for i in range(width):
        for j in range(height):
            if char[j][i] == 0:
                screen[direction[1]+j][direction[0]+i] = 0
            if char[j][i] == 1:
                screen[direction[1]+j][direction[0]+i] = 3
            if char[j][i] == 2:
                screen[direction[1]+j][direction[0]+i] = 6
            if char[j][i] == 3:
                screen[direction[1]+j][direction[0]+i] = 4
            if char[j][i] == 4:
                screen[direction[1]+j][direction[0]+i] = 7

def drawMatrix(array):
    # color = 0 : 'None', 1 : 'Red', 2 : 'Green', 3 : 'Yellow', 4 : 'Blue', 5 : 'Purple', 6 : 'Crystal', 7 : 'White'
    for x in range(len(array[0])):
        for y in range(len(array)):
            LD.set_pixel(x, y, array[y][x])

def consoleMatrix(screen):
        for i in screen:
                    print(i)

iScreen = [[0 for x in range(32)] for y in range(16)]
oScreen=copy.deepcopy(iScreen)


def weather(oScreen):

    #weather data
    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ urllib.parse.quote('+날씨')

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    location= soup.find('div', class_='select_box').find('span', class_='btn_select').text

    temp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
    weather = soup.find('ul', class_="info_list").find('p', class_="cast_txt").text.split(',')[0]
    print(temp)
    print(weather)

#        location= soup.find('div', class_='select_box').find('span', class_='btn_select').text
#        print(location)

    #draw weather icon
    if weather == '맑음':
        drawChar(icons.Sun,oScreen,32,16,(0,0),2)
    elif weather == '흐림':
        drawChar(icon.Fog,oScreen,32,16,(0,0),2)
    elif weather == '구름 많음':
        drawChar(icons.Cloud,oScreen,32,16,(0,0),2)
    elif weather == '비':
        drawChar(icons.Rain,oScreen,32,16,(0,0),2)
    elif weather == '눈':
        drawChar(icons.Snow,oScreen,32,16,(0,0),2)

    # Sets Temperature Color
    if int(temp) <= 0:
        TempColor = 4   #blue 
    elif int(temp) > 31:
        TempColor = 1   #red
    else:
        TempColor = 7   #white

   # Set Temperature Position
    post1=(14,1)
    post2=(18,1)
    post3=(23,1)
    post4=(27,1)

   # Draw Temperature
    if int(temp)<-10:
        drawChar(icons.Minus, oScreen,3,5,post1,TempColor)
        drawChar(numberIcon(temp[1]),oScreen,3,5,post2,TempColor)
        drawChar(numberIcon(temp[2]),oScreen,3,5,post3,TempColor)
        drawChar(icons.Cdegree,oScreen,4,5,post4,TempColor)
    if int(temp)<0:
        drawChar(icons.Minus, oScreen,3,5,post2,TempColor)
        drawChar(numberIcon(temp[1]),oScreen,3,5,post3,TempColor)
        drawChar(icons.Cdegree,oScreen,4,5,post4,TempColor)
    if 0<=int(temp)<10:
        drawChar(numberIcon(temp),oScreen,3,5,post2,TempColor)
        drawChar(icons.Cdegree,oScreen,4,5,post3,TempColor)

    if 10<=int(temp):
        drawChar(numberIcon(temp[0]),oScreen,3,5,post2,TempColor)
        drawChar(numberIcon(temp[1]),oScreen,3,5,post3,TempColor)
        drawChar(icons.Cdegree,oScreen,4,5,post4,TempColor)

    return oScreen

def clock(oScreen):
    now=time.localtime()
    #print('%02d:%02d:%02d'%(now.tm_hour,now.tm_min,now.tm_sec))

    #Set Time number position
    post5=(14,9)
    post6=(18,9)
    post7=(24,9)
    post8=(28,9)
    white=7
    hour=str(now.tm_hour)
    minute=str(now.tm_min)
    second=str(now.tm_sec)
    if (int(hour)<10):
        drawChar(icons.num_0,oScreen,3,5,post5,white)
        drawChar(numberIcon(hour),oScreen,3,5,post6,white)
    elif (int(hour)>10):
        drawChar(numberIcon(hour[0]),oScreen,3,5,post5,white)
        drawChar(numberIcon(hour[1]),oScreen,3,5,post6,white)
    drawChar(icons.Dot,oScreen,3,5,(21,9),white)
    if (int(minute)<10):
        drawChar(icons.num_0,oScreen,3,5,post7,white)
        drawChar(numberIcon(minute),oScreen,3,5,post8,white)
    elif (int(minute)>10):
        drawChar(numberIcon(minute[0]),oScreen,3,5,post7,white)
        drawChar(numberIcon(minute[1]),oScreen,3,5,post8,white)
    #consoleMatrix(oScreen)   
    drawMatrix(oScreen)

count = 0
while True:
    print(count)
    if count % 600 == 0:
        oScreen=copy.deepcopy(iScreen)
        oScreen = weather(oScreen)
    clock(oScreen)
    time.sleep(1)
    count += 1
