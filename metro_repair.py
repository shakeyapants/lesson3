# Определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов
# и вывести на экран их названия.
# Файл с данными можно скачать на странице http://data.mos.ru/opendata/624/row/1773539.

import json
import datetime as dt

# today
today = dt.datetime.today()

# reading json
with open('metro_stops.json', 'r', encoding='windows-1251') as data_file:
    data = json.load(data_file)


# stations with repairs
for i in range(len(data)):
    if data[i]['RepairOfEscalators']:
        date_repair = data[i]['RepairOfEscalators'][0]['RepairOfEscalators']
        station = data[i]['NameOfStation']
        start_of_repair = dt.datetime.strptime(date_repair.split('-')[0], '%d.%m.%Y')
        end_of_repair = dt.datetime.strptime(date_repair.split('-')[-1], '%d.%m.%Y')

        # stations with repairs today
        if start_of_repair <= today <= end_of_repair + dt.timedelta(1):
            print('На станции {} эскалаторы ремонтируются до {}'.format(station, end_of_repair.date()))


