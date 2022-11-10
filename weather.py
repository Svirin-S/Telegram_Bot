import requests
from bs4 import BeautifulSoup


URL = 'https://www.gismeteo.ru/weather-moscow-4368/now/'
HEADERS = {
    'authority': 'log.strm.yandex.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://habr.com',
    'referer': 'https://habr.com/ru/all/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}


def weather():
    res = requests.get(url=URL, headers=HEADERS)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, features='html.parser')  
        temp = soup.find('span', class_='unit unit_temperature_c')  
        return f'Температура в Москве {temp.text}С'


