import re #fuck you Kenny

#Declare some things
part_numbers = []
elf_symbols = ['+', '-', '*', '/', '&', '@', '=', '%', '$', '#']

#Define functions
def symbolcheck(text):
    for c in text:
        if c in elf_symbols: 
            #print(c)
            return True
    return False

def iselfnumber(pos, number, line):
    if line[pos + len(number)].isdigit() or line[pos - 1].isdigit(): return False
    else: return True

def findsymbol(index, part, lines, iter):
    line = lines[index]
    length = len(part) 
    matches = [m for m in re.finditer(part,line) if iselfnumber(m.span()[0],m.group(0),line)]
    match = matches[iter - 1]
    pos = match.span()[0]

    #left
    if pos > 0:
        sym = line[pos - 1]
        if symbolcheck(sym): return True
        
    #right
    sym = line[pos + length]
    if symbolcheck(sym): return True

    #as above
    if index > 0:
        line = lines[index - 1]
        diag = line[max(0,pos - 1):pos + length + 1]
        if symbolcheck(diag): return True
    
    #so below
    if index + 1 < len(lines):
        line = lines[index + 1]
        diag = line[max(0,pos - 1):pos + length + 1]
        if symbolcheck(diag): return True

#Main program
with open ('Working files/Day 3 Data.txt') as file:
    lines = file.readlines()
    
    for index, line in enumerate(lines):
        numbers = re.findall("\d+", line)
        checked = []
        for number in numbers:
            checked.append(number)
            iter = checked.count(number)
            if findsymbol(index,number,lines,iter): 
                part_numbers.append(int(number))
            else: print(f"Line: {index} Number:{number}")

print(sum(part_numbers))
