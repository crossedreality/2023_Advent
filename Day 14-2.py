#This is something that could probably be solved with 2d vector rotation math...
#...but I haven't taken a geometry class in 25 years. 
DIRECTIONS = {
     0: "N",
     1: "W",
     2: "S",
     3: "E"
}
LOOPSTART = 120
LOOPLENGTH = 42
CYCLES = 1000000000
direction = "N"
xbound = 0
ybound = 0
map = None
rockers = set() #These don't move!
rollers = set()
tilts = 4 * CYCLES #There are 4 of my cycles per puzzle 'cycle'
results = set()

#region
def shift(rock: tuple): 
    can,next = CanMove(rock)
    if can:
         rollers.add(next)
         rollers.remove(rock)
         return (True, next)
    else: return (False, rock)

def north(location: tuple): return (location[0], location[1] - 1)
def south(location: tuple): return (location[0], location[1] + 1)
def east(location: tuple): return (location[0] + 1, location[1])
def west(location: tuple): return (location[0] - 1, location[1])
    
def InBounds(location):
    if location:
        x, y = location
        if 0 <= x < xbound and 0 <= y < ybound: return True
        else: return False
    else: return False

def CanMove(location):
    if direction == "N": proposed = north(location)
    elif direction == "S": proposed = south(location)
    elif direction == "E": proposed = east(location)
    elif direction == "W": proposed = west(location)
    
    if (proposed and
        InBounds(proposed) and 
        (proposed not in rockers) and
        (proposed not in rollers)):
                return (True,proposed)
    else: return (False,proposed)

def sortrocks():
    if direction == "N": return sorted(rollers,key=lambda l: l[1])
    elif direction == "S": return sorted(rollers,key=lambda l: l[1], reverse=True)
    elif direction == "W": return sorted(rollers,key=lambda l: l[0])
    elif direction == "E": return sorted(rollers,key=lambda l: l[0], reverse=True)

def value():
    return sum(ybound - r[1] for r in rollers)
#endregion

with open ('Working files/Day 14 Data.txt') as file:
    map = file.read().splitlines()
    ybound = len(map)
    xbound = len(map[0])
    for y,line in enumerate(map):
        for x,character in enumerate(line):
            if character == "O": rollers.add((x,y))
            elif character == "#": rockers.add((x,y))
    
    completed = 0
    for tilt in range(tilts):
        d = tilt % 4 
        direction = DIRECTIONS[d]
        loopset = sortrocks()
        for rock in loopset:
            roll = rock
            rolling = True
            while rolling: rolling,roll = shift(roll)
        if d == 3: 
            completed += 1
        if (completed > LOOPSTART and
            ((CYCLES - LOOPSTART) % LOOPLENGTH) == (completed - LOOPSTART) % LOOPLENGTH):
            print(f"Value of {CYCLES} is {value()}")
            break