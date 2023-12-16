boxes = {}
lenses = []

#region
class Lens:
    def __init__(self, seq):
        self.box = 0
        self.label = self.op = self.focal = ''
        if "=" in seq: self.op = "="
        elif "-" in seq: self.op = "-"

        s = seq.split(self.op)
        for c in s[0]:
            self.box += ord(c)
            self.box *= 17
            self.box %= 256
            self.label += c
        
        if s[1]: self.focal = s[1]  
#endregion

with open ('Working files/Day 15 Data.txt') as file:
    steps = file.read().strip().split(',')
    for step in steps:
        l = Lens(step)
        if l.op == "=": 
            if boxes.get(l.box): 
                if boxes[l.box].get(l.label):
                    boxes[l.box].update({l.label: l.focal})
                else: boxes[l.box].update({l.label: l.focal})
            else:
                boxes.update({l.box: {l.label: l.focal}})
        elif l.op == "-" and boxes.get(l.box) and boxes[l.box].get(l.label): 
            boxes[l.box].pop(l.label)
        lenses.append(l)

    power = 0
    for key, box in boxes.items():
        for lens in box:
            power += (1 + key) * (list(box.keys()).index(lens) + 1) * int(box[lens])

    print(power)