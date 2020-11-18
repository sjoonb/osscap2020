from urllib.request import urlopen, Request
import urllib
from bs4 import BeautifulSoup as bs4

from PIL import Image
from PIL import ImageDraw
import schedule
import time
import requests
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
matrix = RGBMatrix(options = options)

def drawimage(path, x, y):
    image = Image.open(path).convert('RGB')
    image.load()
    matrix.SetImage(image, x, y)

def job():
    # Clear matrix
    matrix.Clear()

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
        #icon = weather['icon']

        #Conditions = weather['id']

        #Draw weather icon
        if weather=='눈':
            drawimage('weathericons/' + 'snow' + '.png', 9, 1)
        elif weather=='비':
            drawimage('weathericons/' + '09d' + '.png', 9, 1)
        elif weather=='맑음':
            drawimage('weathericons/' + '01d' + '.png', 9, 1)
        elif weather=='흐림':
            drawimage('weathericons/' + '03d' + '.png', 9, 1)
        elif weather=='구름많음':
            drawimage('weathericons/' + '02d' + '.png', 9, 1)

        #Draw temperature
        TempComponents = str(temp)
        TempLength = len(TempComponents)

        # Sets Temperature Color
        if temp <= 0:
            TempColor = 'b'
        elif temp > 32:
            TempColor = 'r'
        else:
            TempColor = 'w'

        if TempLength == 1:
            drawimage('numbericons/' + str(TempComponents[0]) + TempColor + '.png', 11, 16)
            drawimage('numbericons/' + 'F' + TempColor + '.png', 17, 16)

        if TempLength == 2:
            drawimage('numbericons/' + str(TempComponents[0]) + TempColor + '.png', 7, 16)
            drawimage('numbericons/' + str(TempComponents[1]) + TempColor + '.png', 13, 16)

            drawimage('numbericons/' + 'F' + TempColor + '.png', 19, 16)

        if TempLength == 3:
            drawimage('numbericons/' + str(TempComponents[0]) + TempColor + '.png', 5, 16)
            drawimage('numbericons/' + str(TempComponents[1]) + TempColor + '.png', 9, 16)
            drawimage('numbericons/' + str(TempComponents[2]) + TempColor + '.png', 15, 16)
            drawimage('numbericons/' + 'F' + TempColor + '.png', 21, 16)

        print('Current Temp: '+str(temp)+' Icon Code: '+str(icon))

    except requests.exceptions.RequestException as e:
       drawimage('weathericons/' + 'error' + '.png', 9, 1)

job()
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
