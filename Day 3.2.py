import re
import math

#Declare some things

#region Functions
def findgear(index, position, lines):
    numbers = []

    #Up
    if index > 0:
        cline = lines[index - 1]
        if cline[max(0,position - 1)].isdigit():
            numbers.append(findnumber(position - 1,cline))
        if cline[position].isdigit():
            numbers.append(findnumber(position, cline))
        if cline[position + 1].isdigit():
            numbers.append(findnumber(position + 1, cline))
    
    #Down
    if index + 1 < len(lines):
        cline = lines[index + 1]
        if cline[max(0,position - 1)].isdigit():
            numbers.append(findnumber(position - 1,cline))
        if cline[position].isdigit():
            numbers.append(findnumber(position, cline))
        if cline[position + 1].isdigit():
            numbers.append(findnumber(position + 1, cline))
    
    #Left
    if line[max(0,position - 1)].isdigit():
        numbers.append(findnumber(position - 1, line))
    
    #Right
    if line[position + 1].isdigit():
        numbers.append(findnumber(position + 1, line))

    numbers = set(numbers) #Symmetric gear ratios be damned
    if len(numbers) == 2:
        return math.prod(numbers)
    else: print(f"Line: {index + 1} Numbers: {numbers}")

def findnumber(position, line):
    start = position
    while line[start].isdigit():
        start -= 1
    else: start += 1
    
    end = position
    while line[end].isdigit():
        end += 1

    return int(line[start:end])
#endregion

#Main 
ratios = []

with open ('Working files/Day 3 Data.txt') as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        stars = re.finditer('\*', line)
        for star in stars:
            gear = findgear(index, star.start(), lines)
            if gear: ratios.append(gear)

print(sum(ratios))
