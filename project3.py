#!/usr/bin/env python3

"""
Created on Mon Feb 14 16:27:13 2022
#make it count the lines of code and the lines for the last 6 months
@author: moises
"""
with open("http_access_log.txt") as file_in:
    array = []
    for line in file_in:
        array.append(line)

count = 0

for i in array:
    if i.find("Apr") != -1 and i.find("1995") != -1 and i.find("[11") != -1:
        count += 1
    elif i.find("May") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jun") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jul") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Aug") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Sep") != -1 and i.find("1995") != -1:
        count += 1
        array[count] = i
    elif i.find("Oct") != -1 and i.find("1995") != -1:
        count += 1

countall = len(array)

print("Total Number of Requests in the past six months: ", count)
print("Total Number of Requests: ", countall)

