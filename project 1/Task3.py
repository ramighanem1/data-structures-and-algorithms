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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
"""
called_area = []
for record in calls:
    if record[0][:5]=="(080)":
        if record[1][0]=='(':
            called_area.append(record[1][:record[1].find(")")+1])
        elif record[1][:3]=='140':
            called_area.append('140')
        else:
            called_area.append(record[1][:4])

            
# to remove duplicates
called_area2=set(called_area)

'''
print("The numbers called by people in Bangalore have codes : ")
for i in called_area2:
    print(i)
'''


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""



x=0
y=0

for i in called_area:
    y+=1
    if i=="(080)":
        x+=1
percentage=x/y
percentage=percentage*100
print("{0:.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))


            
            
    













