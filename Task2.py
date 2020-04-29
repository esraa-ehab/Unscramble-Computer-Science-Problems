"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from itertools import chain
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
tel_nums = dict()
call_time = 0

for caller, reciever, duration, timestamp in calls:
    date = datetime.strptime(timestamp, '%d-%m-%Y %H:%M:%S')
    if date.year ==2016 and date.month == 9:
        tel_nums[caller] += int(duration)
        tel_nums[reciever] += int(duration)

longest_duration = max(tel_nums.items(), key = lambda x: x[1])
print('{} spent the longeat time, {} seconds, on the phone during September 2016.'.format(longest_duration))