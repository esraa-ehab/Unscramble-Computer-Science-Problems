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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

nums = [call[0] for call in calls]
recieves = [call[1] for call in calls]
people = set()

for text, receive in zip(texts, recieves):
    for i in range (0, 2):
        people.add(text[i])
    people.add(receive)

telemarketers = {call for call in nums if call not in people}
telemarketers = sorted(list(telemarketers))

print('These numbers could be telemarketers: {}'.format(telemarketers))
print('Total potential telemarketers: {}'.format(telemarketers))