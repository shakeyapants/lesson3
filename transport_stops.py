# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок,
# вывести улицу, на которой больше всего остановок.


import csv

# dict {street1 : [stop1, stop2 ...], street2 : [stop1, stop2...]}
stops = {}


# reading csv file, making stops dictionary and counting total number of stops
with open('stops_data.csv', 'r', encoding='Windows-1251') as f:
    csvreader = csv.DictReader(f, delimiter=';')
    num_stops = 0
    for row in csvreader:
        num_stops += 1
        if not row['Street'] in stops:
            stops[row['Street']] = [row['Name']]
        else:
            stops[row['Street']].append(row['Name'])

    print('Количество остановок: {}'.format(num_stops))

max_stops_street = 0
street_with_max_stops = None


# determination of the street with the maximum number of stops
for street in stops:
    stops_street = len(stops.get(street))
    if stops_street > max_stops_street:
        max_stops_street = stops_street
        street_with_max_stops = street

print('Больше всего остановок на улице: {}'.format(street_with_max_stops))