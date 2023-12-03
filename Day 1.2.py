final = []

def elf_translator(line):
    elf_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    def elf_inserter(line, pos, num):
        return line[:pos] + num + line[pos:]

    firstpos = len(line)
    lastpos = 0
    first = 1
    last = 1
    for k in elf_words.keys():
        pos = line.find(k)
        if pos != -1 and pos < firstpos: 
            firstpos = pos
            first = elf_words[k]
    for k in elf_words.keys():
        pos = line.rfind(k)
        if pos != -1 and pos > lastpos:
            lastpos = pos
            last = elf_words[k]
    if firstpos != len(line): line = elf_inserter(line, firstpos, first)
    if lastpos > 0 and lastpos != firstpos: line = elf_inserter(line, lastpos + 1, last) #Add one because we've already shifted the index if we're this far
    return line

with open ('Working files/Day 1 Calibration.txt') as file:
    for line in file:
        numbers = []
        line = elf_translator(line)
        for c in line:
            if c.isdigit(): numbers.append(c)
        count = len(numbers)
        first = numbers[0] #We know all of these have at least one number, but some don't have two.
        if count > 1: second = numbers[count - 1]
        else: second = numbers[0]
        linevalue = int(first + second)
        final.append(linevalue)
print(sum(final))
