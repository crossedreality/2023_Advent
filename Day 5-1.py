from collections import defaultdict

#region Constants
ITERATIONS = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
#endregion

#region Classes
class Map:
    def __init__(self, source, destination, range, type):
        self.source = int(source)
        self.destination = int(destination)
        self.range = int(range)
        self.type = type

    def InRange(self, sourcenum):
        if int(sourcenum) in range(self.source, self.source + self.range): return True
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
#endregion

#Main 
seeds = []
maps = defaultdict(list)
locations = []

with open ('Working files/Day 5 Data.txt') as file:
    current_type = None

    for i,line in enumerate(file):
        if i == 0:
            seeds = [int(i) for i in line.partition(":")[2].split()]

        elif "map:" in line:
            current_type = line.split("-")[2].partition(" map:")[0]
        
        else:
            parse = line.strip().split()
            if parse: maps[current_type].append(Map(parse[1],parse[0],parse[2],current_type))

for seedvalue in seeds:
    for iteration in ITERATIONS:
        seedvalue = findmap(seedvalue, iteration, maps)
        if (iteration == "location"): locations.append(seedvalue)

print(min(locations))