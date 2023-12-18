from enum import Enum

xbound = 0
ybound = 0
elements = {}

#region
class Direction(Enum):
     N = 0
     S = 1
     E = 2
     W = 3

class Beam:
     def __init__(self, direction, location):
          self.direction = direction
          self.location = location

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

def AlreadySpawned(beam):
    if (beam.location,beam.direction) in spawned: return True
    else: return False

def Move(beam):
    if beam.direction == Direction.N: proposed = north(beam.location)
    elif beam.direction == Direction.S: proposed = south(beam.location)
    elif beam.direction == Direction.E: proposed = east(beam.location)
    elif beam.direction == Direction.W: proposed = west(beam.location)
    
    if proposed and InBounds(proposed):
        beam.location = proposed
        energized.add(proposed)
        if proposed in elements.keys():
            et = elements[proposed]
            if et == "/":
                if beam.direction == Direction.E: beam.direction = Direction.N
                elif beam.direction == Direction.N: beam.direction = Direction.E
                elif beam.direction == Direction.W: beam.direction = Direction.S
                elif beam.direction == Direction.S: beam.direction = Direction.W
            elif et == "\\":
                if beam.direction == Direction.E: beam.direction = Direction.S
                elif beam.direction == Direction.N: beam.direction = Direction.W
                elif beam.direction == Direction.W: beam.direction = Direction.N
                elif beam.direction == Direction.S: beam.direction = Direction.E
            elif et == "-":
                if beam.direction == Direction.N or beam.direction == Direction.S:
                    beam.direction = Direction.W
                    nb = Beam(Direction.E,proposed)
                    if not AlreadySpawned(nb): 
                        beams.append(nb)
                        spawned.add((nb.location,nb.direction))
            elif et == "|":
                 if beam.direction == Direction.E or beam.direction == Direction.W:
                    beam.direction = Direction.N
                    nb = Beam(Direction.S,proposed)
                    if not AlreadySpawned(nb): 
                        beams.append(nb)
                        spawned.add((nb.location,nb.direction))
            spawncheck = AlreadySpawned(beam)
            if spawncheck: return None
            elif not spawncheck: spawned.add((proposed, beam.direction))
        return proposed
    else: return None
#endregion

with open ('Working files/Day 16 Data.txt') as file:
    map = file.read().splitlines()
    ybound = len(map)
    xbound = len(map[0])
    for y,line in enumerate(map):
        for x,character in enumerate(line):
            if character in { "/", "\\", "|", "-"}: elements.update({(x,y): character})

    results = []
    biggerbeams = []
    for i in range (0,ybound): biggerbeams.append(Beam(Direction.E, (-1,i)))
    for i in range (0,ybound): biggerbeams.append(Beam(Direction.W, (xbound,i)))
    for i in range (0,xbound): biggerbeams.append(Beam(Direction.S, (i,-1)))
    for i in range (0,xbound): biggerbeams.append(Beam(Direction.N, (i,ybound)))

    for bigbeam in biggerbeams:
        energized = set()
        spawned = set()
        beams = [bigbeam]
        bigbeam.location = Move(bigbeam)

        for beam in beams:
            beam.location = Move(beam)
            while InBounds(beam.location): beam.location = Move(beam)        
        results.append(len(energized))
    
    print(max(results))