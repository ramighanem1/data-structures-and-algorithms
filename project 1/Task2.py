"""
Read file into texts and calls.
"""
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
"""
calls_dictionary = {}
for caller, reciever, timestamp, duration in calls:
    if caller not in calls_dictionary.keys():
        calls_dictionary[caller]=0
    if reciever not in calls_dictionary.keys():
        calls_dictionary[reciever]=0
    date = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        calls_dictionary[caller] += int(duration)
        calls_dictionary[reciever] += int(duration)

long=0
telephone=0
for key,value in calls_dictionary.items():
    if value>long:
        telephone=key
        long=value
    
        
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(telephone,long))

