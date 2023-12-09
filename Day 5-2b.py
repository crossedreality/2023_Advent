from collections import defaultdict

#region Constants
ITERATIONS = ["location", "humidity", "temperature", "light", "water", "fertilizer", "soil"]
#endregion

#region Classes
class Map:
    def __init__(self, source, destination, range, type):
        self.source = int(source)
        self.destination = int(destination)
        self.smax = self.source + int(range)
        self.type = type

    def InRange(self, sourcenum):
        sourcenum = int(sourcenum)
        if self.source <= sourcenum <= self.smax: return True
        else: return False
    
    def value(self, sourcenum):
        difference = self.destination - self.source
        return sourcenum + difference
#endregion

#region Functions
def findmap(value, key, maps):
    mapvalue = next((m.value(value) for m in maps[key] if m.InRange(value)), None)
    if mapvalue: return mapvalue
    else: return value

def procseed(seed, maps):
    for iteration in ITERATIONS:
            seed = findmap(seed, iteration, maps)
            if (iteration == "soil"): return seed

def psrange(seed, seeds):
    for range in seeds:
        if range[0] <= seed <= range[1]: return True
#endregion

seeds = []
locations = []
maps = defaultdict(list)

with open ('Working files/Day 5 Data.txt') as file:
    current_type = None

    for i,line in enumerate(file):
        if i == 0:
            packets = [int(i) for i in line.partition(":")[2].split()]
            s = 0 #This type of loop isn't 'pythonic' but I don't care
            while s < len(packets):
                startseed = packets[s]
                endseed = startseed + packets[s + 1]
                seeds.append((startseed, endseed))
                s += 2

        elif "map:" in line:
            current_type = line.split("-")[2].partition(" map:")[0]
        
        else:
            parse = line.strip().split()
            if parse: maps[current_type].append(Map(parse[0],parse[1],parse[2],current_type))

found = False
location = 0
while found == False:
    seed = procseed(location, maps)
    if psrange(seed,seeds): found = True
    else: location += 1

print(location)