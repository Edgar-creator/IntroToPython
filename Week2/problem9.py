import time
import calendar
import datetime
tday = datetime.datetime.now()
print(tday)
print(tday.year)
print(tday.month)
print(datetime.date.today().isoweekday())
tdelta = datetime.timedelta(days = 5)
print(tday - tdelta)
print(tday + tdelta)