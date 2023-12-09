from math import prod

#region Functions
def boatrace(time, distance):
    victories = 0
    for i in range(time): 
        if (i * (time - i) > distance): victories += 1
    return victories
#endregion

with open ('Working files/Day 6 Data.txt') as file:
    lines = file.readlines()
    time = int(lines[0].partition(":")[2].replace(" ",""))
    distance = int(lines[1].partition(":")[2].replace(" ",""))
    print(boatrace(time,distance))