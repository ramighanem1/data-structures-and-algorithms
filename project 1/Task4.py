"""
Read file into texts and calls.
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
"""
not_telemarketers=set()
telemarketers=set()

for record in texts:
    not_telemarketers.add(record[0])
    not_telemarketers.add(record[1])

for record in calls:
    not_telemarketers.add(record[1])

for record in calls:
    if record[0] not in not_telemarketers:
            telemarketers.add(record[0])

        
    

print("These numbers could be telemarketers: ")
for x in telemarketers:
    print(x)

