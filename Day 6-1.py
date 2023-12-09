from math import prod

#region
records = []
#endregion

#region Functions
def boatrace(time, distance):
    victories = 0
    for i in range(time): 
        if (i * (time - i) > distance): victories += 1 #append if 6-2 needs it
    return victories
#endregion

with open ('Working files/Day 6 Data.txt') as file:
    lines = file.readlines()
    times = [int(t) for t in lines[0].partition(":")[2].split()]
    distances = [int(d) for d in lines[1].partition(":")[2].split()]
    wins = []

    for i in range(len(times)):
        records.append((times[i], distances[i]))

    for record in records:
        wins.append(boatrace(record[0],record[1]))

print(prod(wins))