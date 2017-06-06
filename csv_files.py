# Возьмите словарь с ответами из функции get_answer
# Запишите его содержимое в формате csv в формате: "ключ"; "значение". Каждая пара ключ-значение должна располагаться на отдельной строке

import csv

# словарь из функции get_answer
answers = {'hi': 'Hey', 'how are you?': 'Fine', 'bye': 'See you'}

answers_list = []

# получаем лист из словарей, где ключами являются названия колонок
for key, value in answers.items():
    answers_list.append({'key': key, 'value': answers[key]})

# запись csv файла
with open('get_answer.csv', 'w', encoding='utf-8') as f:
    fields = ['key', 'value']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for pair in answers_list:
        writer.writerow(pair)