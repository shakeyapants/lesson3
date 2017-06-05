# 1. Напечатайте в консоль даты: вчера, сегодня, месяц назад

import datetime as dt

# set today
today = dt.datetime.now()

# print yesterday
yesterday = today - dt.timedelta(days=1)
print('Yesterday was ' + yesterday.strftime('%d-%m-%Y'))

# print today
print('Today is ' + today.strftime('%d-%m-%Y'))

# month ago
def monthdelta(date, delta):
    month, year = (date.month + delta) % 12, date.year + ((date.month) + delta-1) // 12
    if not month:
        month = 12
    day = min(date.day, [31, 29 if year % 4 == 0 and not year % 400 == 0 else 28,31,30,31,30,31,31,30,31,30,31][month-1])
    return date.replace(day=day, month=month, year=year)


month_ago = monthdelta(today, -1)
print('Month ago was ' + month_ago.strftime('%d-%m-%Y'))


# 2. Превратите строку "01/01/17 12:10:03.234567" в объект datetime

s = "01/01/17 12:10:03.234567"
date_dt = dt.datetime.strptime(s, '%d/%m/%y %H:%M:%S.%f')
print('Datetime object of the given string is {}'.format(date_dt))