from copy import deepcopy
from itertools import combinations

magicn = 999999
offsets = []

#region
def getcolumn(map, index) -> list:
    column = []
    for r in map: column.append(r[index])
    return column

def expand(map):
    for i in range(len(map[0])):
        col = getcolumn(map, i)
        if not "#" in col: offsets.append(((i,0), magicn))

    for i,r in enumerate(map):
        if not "#" in r: offsets.append(((0,i), magicn))

def getdistance(p1, p2):
    x1 = abs(p1[0] - p2[0])
    y1 = abs(p1[1] - p2[1])
    return x1 + y1

def getoffset(location):
    xo = sum([o for key, o in offsets if key[0] < location[0] and key[1] == 0])
    yo = sum([o for key, o in offsets if key[1] < location[1] and key[0] == 0])
    return ((location[0] + xo,location[1] + yo))
#endregion

with open ('Working files/Day 11 Data.txt') as file:
    universe = file.read().splitlines()
    expand(universe)

    galaxies = []
    for y,r in enumerate(universe):
        for x,c in enumerate(r):
            if c == "#":
                galaxies.append(getoffset((x,y)))    
    pairs = list(combinations(galaxies,2)) #lol there's a library for this
    
    distances = []
    for pair in pairs:
        distances.append(getdistance(pair[0], pair[1]))
    
    print(sum(distances))