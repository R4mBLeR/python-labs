import re
import time
import csv

import requests
from bs4 import BeautifulSoup


class Concert:
    def __init__(self, name, date, _time, place, min_price, max_price, age_limit):
        self.name = name
        self.date = date
        self.time = _time
        self.place = place
        self.min_price = min_price
        self.max_price = max_price
        self.age_limit = age_limit

    @property
    def avg_price(self):
        if self.min_price is None and self.max_price is None:
            return None
        if self.min_price is None:
            return self.max_price
        if self.max_price is None:
            return self.min_price
        return (self.min_price + self.max_price) / 2


def text_of(tag):
    return tag.text.strip() if tag else None


page = requests.get('https://afisha.relax.by/conserts/minsk/', timeout=10)
soup = BeautifulSoup(page.text, "html.parser")
concerts = soup.find_all('div', class_='schedule__table--movie__item')
print("Карточек на странице:", len(concerts))

live_concerts = []

for concert in concerts:
    link = None
    try:
        link_tag = concert.find('a', class_='js-schedule__event-link schedule__event-link link')
        if not link_tag:
            continue
        link = link_tag['href']

        page = requests.get(link, timeout=10)
        soup = BeautifulSoup(page.text, "html.parser")
        data = soup.find('div', class_='b-afisha-layout-theater_full')
        if not data:
            continue

        name = text_of(data.find('h1', class_='b-afisha-layout-theater_movie-title'))

        date_tag = data.find('div', class_='schedule__day schedule__day--fill')
        meta = date_tag.find('meta') if date_tag else None
        date = meta['content'].strip() if meta and meta.has_attr('content') else None

        place = text_of(data.find('div', class_='schedule__place-title-row'))
        _time = text_of(data.find('span', class_='schedule__seance-time'))

        min_price = max_price = age_limit = None
        for li in data.find_all('li'):
            span = li.find('span', class_='b-afisha_cinema_description_table_desc')
            if not span:
                continue
            if 'Стоимость' in li.text and min_price is None:
                numbers = re.findall(r'\d+(?:[.,]\d+)?', span.text)
                if numbers:
                    min_price = float(numbers[0].replace(',', '.'))
                    max_price = float(numbers[-1].replace(',', '.')) if len(numbers) > 1 else min_price
            if 'Возрастное ограничение:' in li.text:
                age_limit = span.text.strip().rstrip('.')

        live_concerts.append(Concert(name, date, _time, place, min_price, max_price, age_limit))
        print("Обработан:", name)
        time.sleep(0.1)
    except Exception as e:
        print("Ошибка на", link, e)


prices = [c.avg_price for c in live_concerts if c.avg_price is not None]
priced = [c for c in live_concerts if c.avg_price is not None]

total = len(live_concerts)
min_price_all = min(prices) if prices else None
max_price_all = max(prices) if prices else None
avg_price_all = sum(prices) / len(prices) if prices else None

places = {}
for c in live_concerts:
    if c.place:
        places[c.place] = places.get(c.place, 0) + 1
busiest_place = max(places, key=places.get) if places else None
busiest_count = places.get(busiest_place, 0) if busiest_place else 0

cheapest = min(priced, key=lambda c: c.avg_price) if priced else None
most_expensive = max(priced, key=lambda c: c.avg_price) if priced else None


print(f"Всего мероприятий: {total}")
print(f"Минимальная стоимость билета: {min_price_all}")
print(f"Максимальная стоимость билета: {max_price_all}")
print(f"Средняя стоимость билета: {avg_price_all}")
print(f"Самая загруженная площадка: {busiest_place} ({busiest_count} мероприятий)")
if cheapest:
    print(f"Самый дешёвый билет: {cheapest.name} {cheapest.avg_price} ({cheapest.place})")
if most_expensive:
    print(f"Самый дорогой билет: {most_expensive.name} {most_expensive.avg_price} ({most_expensive.place})")


with open('concerts.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Название', 'Дата', 'Время', 'Место',
                     'Мин. цена', 'Макс. цена', 'Возраст'])
    for c in live_concerts:
        writer.writerow([c.name, c.date, c.time, c.place,
                         c.min_price, c.max_price, c.age_limit])
    writer.writerow([])
    writer.writerow(['ИТОГИ'])
    writer.writerow(['Всего мероприятий', total])
    writer.writerow(['Мин. стоимость', min_price_all])
    writer.writerow(['Макс. стоимость', max_price_all])
    writer.writerow(['Средняя стоимость', avg_price_all])
    writer.writerow(['Самая загруженная площадка', f"{busiest_place} ({busiest_count})"])
    if cheapest:
        writer.writerow(['Самый дешёвый билет', f"{cheapest.name} - {cheapest.avg_price}"])
    if most_expensive:
        writer.writerow(['Самый дорогой билет', f"{most_expensive.name} - {most_expensive.avg_price}"])

print("\nРезультат сохранён в concerts.csv")