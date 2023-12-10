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

pos = 0
steps = 0
end = len(path) - 1
current = "AAA"
while current != "ZZZ":
    d = path[pos]
    instruction = map[current]
    if d == "L": current = instruction[0]
    elif d == "R": current = instruction[1]
    if pos == end: pos = 0
    else: pos += 1
    steps += 1

print(steps)