from datetime import datetime
from datetime import timedelta

print(datetime.now() - timedelta(seconds = 60) + timedelta(weeks = 104))
time_object = timedelta(days = 100, hours = 10, minutes = 13)
print(time_object)

def func(feet, inches):
    print(f'{feet} feet and {inches} inches @ {time_object}')

func(5, 6)
