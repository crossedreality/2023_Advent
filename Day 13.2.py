mirrors = []

#region
class Pattern:
    def __init__(self, pattern, id):
        self.pattern = pattern.split("\n")
        self.id = id
        self.start = -1
        self.orientation = None
        self.GetOrientation(self.pattern)

    def GetOrientation(self, map, tolerance = 0, depth = 0):
        ybound = len(map) - 1
        xbound = len(map[0]) - 1

        for i in range(ybound):
            ltol = tolerance
            ldepth = depth
            reflect = smudge(map[i], map[i + 1])
            if reflect <= ltol:
                if reflect > 0: ltol -= 1
                reflecting = True
                distance = 1
                while reflecting:
                    if (i - distance) >= 0 and (i + 1 + distance) <= ybound:
                        reflect = smudge(map[i - distance],map[i + 1 + distance])
                        if reflect <= ltol:
                            if reflect > 0: ltol -= 1
                            distance += 1
                        else:
                            reflecting = False
                    else:
                        if ldepth == 0 or ltol != tolerance:
                            reflecting = False
                            self.start = i
                            self.orientation = "H"
                            return "H"
                        else:
                            reflecting = False
                            ldepth -= 1
                                
        for i in range(xbound):
            ltol = tolerance
            ldepth = depth
            reflect = smudge(getcolumn(map, i),getcolumn(map, i + 1))
            if reflect <= ltol:
                if reflect > 0: ltol -= 1
                reflecting = True
                distance = 1
                while reflecting:
                    if (i - distance) >= 0 and (i + 1 + distance) <= xbound:
                        reflect = smudge(getcolumn(map, i - distance),getcolumn(map, i + 1 + distance))
                        if reflect <= ltol:
                            if reflect > 0: ltol -= 1
                            distance += 1
                        else: reflecting = False
                    else:
                        if ldepth == 0 or ltol != tolerance:
                            reflecting = False
                            self.start = i
                            self.orientation = "V"
                            return "V"
                        else:
                            reflecting = False
                            ldepth -= 1
        return "Q"
                    
    def value(self) -> int:
        if self.orientation == "H": return (1 + self.start) * 100
        elif self.orientation == "V": return 1 + self.start
        else: return 0

def getcolumn(map, index) -> list:
    column = []
    for r in map: column.append(r[index])
    return column

def smudge(s1, s2):
    return sum (1 for a,b in zip(s1, s2) if a != b)
#endregion

with open ('Working files/Day 13 Data.txt') as file:
    patterns = file.read().split("\n\n")
    for i,map in enumerate(patterns):
        mirrors.append(Pattern(map, i))

    print(f"Clean: {sum([m.value() for m in mirrors])}")

    for m in mirrors:
         m.Orientation = m.GetOrientation(m.pattern,1,1)
    
    print(f"Dirty: {sum([m.value() for m in mirrors])}")