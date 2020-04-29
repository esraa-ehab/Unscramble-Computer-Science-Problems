"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_numbers = []
for text in texts:
    unique_numbers.update(text[:3]) #insert a list 
for call in calls:
    unique_numbers.update(call[:3]) #insert a list

print('There arem {} different telephone numbers in the records.'.format(len(unique_numbers)))