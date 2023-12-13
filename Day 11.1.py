from copy import deepcopy
from itertools import combinations

#region
class Map: 
    def __init__(self, map) -> None:
        self.map = deepcopy(map)

    def getcolumn(self, index) -> list:
        column = []
        for r in self.map: column.append(r[index])
        return column

    def insertcolumn(self, index, content):
        for i,r in enumerate(self.map):
            self.map[i] = r[:index] + content[i] + r[index:]
#endregion

#region
def expand(map):
    newmap = Map(map)
    cc = rc = 0

    for i in range(len(map[0])):
        col = newmap.getcolumn(i + cc)
        if not "#" in col:
            newmap.insertcolumn(i + cc, col)
            cc += 1

    map = deepcopy(newmap.map)

    for i,r in enumerate(map):
        if not "#" in r:
            newmap.map.insert(i + rc, r)
            rc += 1

    return newmap

def getdistance(p1, p2):
    x1 = abs(p1[0] - p2[0])
    y1 = abs(p1[1] - p2[1])
    return x1 + y1
#endregion

with open ('Working files/Day 11 Data.txt') as file:
    universe = file.read().splitlines()
    universe = expand(universe) #expand the map

    galaxies = []
    for y,r in enumerate(universe.map):
        for x,c in enumerate(r):
            if c == "#": galaxies.append((x,y))    
    pairs = list(combinations(galaxies,2)) #lol there's a library for this
    
    distances = []
    for pair in pairs:
        distances.append(getdistance(pair[0], pair[1]))
    
    print(sum(distances))