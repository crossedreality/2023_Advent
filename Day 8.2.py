from math import lcm #I don't know that there's a general solution

path = None
map = {}

with open ('Working files/Day 8 Data.txt') as file:
    for i,line in enumerate(file):
        if i == 0:
            path = line.strip()
        else:
            m = line.strip().partition("=")
            node = m[0].strip()
            if node: 
                route = m[2].replace(" ","")[1:-1].split(",")
                route = (route[0],route[1])
                map.update({node: route})

starts = [s for s in map.keys() if s.endswith("A")]
end = len(path) - 1
multiples = []

def getstep(d, key):
    instruction = map[key]
    if d == "L": return instruction[0]
    elif d == "R": return instruction[1]

for node in starts:
    pos = 0
    steps = 0
    ghosted = False
    while not ghosted:
        d = path[pos]
        node = getstep(d,node)
        if pos == end: pos = 0
        else: pos += 1
        steps += 1
        if node.endswith("Z"):
            ghosted = True
            multiples.append(steps)

print(lcm(*multiples))