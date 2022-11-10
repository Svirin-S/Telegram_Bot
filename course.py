import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

def course():   
    data = requests.get(url=url).json()
    course = (data['Valute']['USD']['Value'])
    return f'Курс доллара {round(course, 2)} р.'
 


  