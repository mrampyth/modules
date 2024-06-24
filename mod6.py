from datetime import datetime
import sys

for line in sys.stdin:
    data = line.strip().split("#")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
    date = datetime.today()
    time = datetime.now().time()
    print(f'{item}\t{cost} at {time} on {date}')


