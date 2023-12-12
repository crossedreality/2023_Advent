#region
NPIPES = ["|", "L", "J"]
SPIPES = ["|", "7", "F"]
EPIPES = ["-", "L", "F"]
WPIPES = ["-", "J", "7"]
looptiles = {}
enclosedtiles = []
#endregion

#region
map = None
results = []
xbound = 0
ybound = 0
class Tile:
    def __init__(self, location: tuple, distance: int, entrance = None):
        self.glyph = tile(location)
        self.location = location
        self.distance = distance
        self.entrance = entrance
#endregion

#region
def north(location: tuple): 
    l = (location[0], location[1] - 1)
    if IsInBounds(l):
        return l
def south(location: tuple):
    l = (location[0], location[1] + 1)
    if IsInBounds(l):
        return l
def east(location: tuple):
    l = (location[0] + 1, location[1])
    if IsInBounds(l):
        return l
def west(location: tuple):
    l = (location[0] - 1, location[1])
    if IsInBounds(l):
        return l
def tile(location): 
    if location: return map[location[1]][location[0]]

def IsInBounds(location):
    if location:
        x, y = location
        if 0 <= x <= xbound and 0 <= y <= ybound: return True
        else: return False
    else: return False

def lookahead(tile):
    options = []
    if tile.glyph in NPIPES: options.append(north(tile.location))
    if tile.glyph in SPIPES: options.append(south(tile.location))
    if tile.glyph in EPIPES: options.append(east(tile.location))
    if tile.glyph in WPIPES: options.append(west(tile.location))
    return [t for t in options if t != tile.entrance][0]

def getstart(start: Tile): #There has to be a better way to this conditional but I'm sleepy and rushing 
    if tile(north(start.location)) in SPIPES: return Tile(north(start.location), 1, start.location)
    elif tile(south(start.location)) in NPIPES: return Tile(south(start.location), 1, start.location)
    elif tile(east(start.location)) in WPIPES: return Tile(east(start.location), 1, start.location)
    elif tile(west(start.location)) in EPIPES: return Tile(west(start.location), 1, start.location)
#endregion

with open ('Working files/Day 10 Data.txt') as file:
    map = file.read().splitlines()
    ybound = len(map)
    xbound = len(map[0])
    y = next((i for i,s in enumerate(map) if "S" in s))
    x = next((i for i,s in enumerate(map[y]) if "S" == s))
    start = Tile((x,y), 0)
    marker = getstart(start)
    looptiles.update({marker.location: marker})

    while marker.glyph != "S":
        next = lookahead(marker)
        marker = Tile(next, marker.distance + 1, marker.location)
        looptiles.update({marker.location: marker})

#region This shit again
    SPIPES.append("S") #Works for me!
    for y in range(ybound): 
        inside = False
        for x in range(xbound):
            if (x, y) in looptiles:
                if tile((x,y)) in SPIPES: inside = not inside
            elif inside:
                enclosedtiles.append((x,y))
    print(len(enclosedtiles))
#endregion