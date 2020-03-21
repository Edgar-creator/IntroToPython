import datetime
import time
import calendar
bday = datetime.date(1996,8,15)
print(bday)
print(bday.year)
print(bday.month)
print(bday.day)
print(bday.weekday())
print(datetime.date(2020,8,15) - datetime.date.today())
print(calendar.month(2017,5))
tdelta = datetime.timedelta(days = 1)
print(datetime.datetime.today() - tdelta)
yes_day = datetime.datetime.today() - tdelta
print(yes_day + 2 * tdelta)
print(yes_day - 3 * tdelta)