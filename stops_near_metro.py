# посчитать, у какой станции метро больше всего остановок (в радиусе 0.5 км)

import json
import csv
from geopy.distance import vincenty

# list of coordinates of stops - names are not important
stops_coordinates = []
# dict of metro stops
metro_coordintes = {}


# reading json metro stops
with open('metro_stops.json', 'r', encoding='windows-1251') as data_file:
    metro_data = json.load(data_file)


# filling dictionary with metro - coordinates
for i in range(len(metro_data)):
    if not metro_data[i]['NameOfStation'] in metro_coordintes:
        metro_coordintes[metro_data[i]['NameOfStation']] = [metro_data[i]['geoData']['coordinates']]
    else:
        metro_coordintes[metro_data[i]['NameOfStation']].append(metro_data[i]['geoData']['coordinates'])


# reading csv file, making stops dictionary and counting total number of stops
with open('stops_data.csv', 'r', encoding='windows-1251') as f:
    csvreader = csv.DictReader(f, delimiter=';')
    for row in csvreader:
        stops_coordinates.append(row['geoData'].split('[')[1].strip(']}'))


max_stops = 0
station = None

# which metro has the most stops
for key, value in metro_coordintes.items():
    for coordinates in value:
        stops_near_one_metro = 0
        metro = (coordinates[0], coordinates[1])
        for stop in stops_coordinates:
            distance = vincenty(metro, stop).meters
            if distance <= 500:
                stops_near_one_metro += 1
        if stops_near_one_metro >= max_stops:
            max_stops = stops_near_one_metro
            station = key

print('Самое большое количество остановок у станции {} – {}'.format(station, max_stops))
