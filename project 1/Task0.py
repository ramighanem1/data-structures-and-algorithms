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
TASK 0:
What is the first record of texts and what is the last record of calls?
"""



print("First record of texts, {0} texts {1} at time {2}".format(texts[0][0],texts[0][1],texts[0][2]))
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(calls[len(calls)-1][0],calls[len(calls)-1][1],calls[len(calls)-1][2],calls[len(calls)-1][3]))

