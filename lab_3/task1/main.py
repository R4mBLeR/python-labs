import time

import requests
from bs4 import BeautifulSoup

page = requests.get('https://afisha.relax.by/conserts/minsk/')
soup = BeautifulSoup(page.text, "html.parser")


class Concert:
    def __init__(self, name, date, time, place, min_price, max_price, age_limit):
        self.name = name
        self.date = date
        self.time = time
        self.place = place
        self.min_price = min_price
        self.max_price = max_price
        self.age_limit = age_limit


live_concerts = []

concerts = soup.find_all('div', class_='schedule__table--movie__item')
for concert in concerts:
    print('Обработан 1 концерт')
    try: 
        link = concert.find('a', class_='js-schedule__event-link schedule__event-link link')['href']
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        data = soup.find('div', class_='b-afisha-layout-theater_full')

        name = data.find('h1', class_='b-afisha-layout-theater_movie-title').text.strip()
        date = data.find('div', class_='schedule__day schedule__day--fill').find('meta')['content'].strip()
        place = data.find('div', class_='schedule__place-title-row').text.strip()
        _time = data.find('span', class_='schedule__seance-time').text.strip()
        min_price = None
        max_price = None
        max_price = None
        age_limit = None
        features = data.find('div', class_='b-ps-features').find('ul')
        for li in soup.find_all('li'):
            if 'Стоимость' in li.text:
                price_span = li.find('span', class_='b-afisha_cinema_description_table_desc')
                if price_span:
                    price_text = price_span.text.strip()
                    partitions = price_text.partition('—')
                    min_price = partitions[0].strip().replace(',', '.')
                    max_price = partitions[2].strip().split(' ')[0].replace(',', '.')
                    break
        if 'Возрастное ограничение:' in li.text:
                        age_span = li.find('span', class_='b-afisha_cinema_description_table_desc')
                        if age_span:
                            age_limit = age_span.text[:-1]
                            break
        live_concerts.append(Concert(name,date,_time,place,min_price,max_price,age_limit))
        time.sleep(0.1)
    except:
        pass

print(live_concerts)
