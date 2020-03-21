num_y = int(input("years "))
num_d = int(input("days "))
import datetime
day = datetime.datetime(2020,5,6,5,6,5,6)
print("Current date:",day)
print("Given years: ",num_y)
print("Given days: ",num_d)
tdelta = datetime.timedelta(days = num_d + num_y * 365)
print("Final date: ",day + tdelta)