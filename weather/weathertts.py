from urllib.request import urlopen, Request
import urllib
import bs4

def weather_tts():
    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ urllib.parse.quote('+날씨')
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    location = soup.find('div', class_='select_box').find('span', class_='btn_select').text
    temp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text

    info = soup.find('ul', class_="info_list").find('p', class_="cast_txt").text.split(', ')[1].split(' ')
    #['어제', '기온과', '같음']
    temp_info = info[1][0]
    diff_info = info[2] #높아요, 낮아요
