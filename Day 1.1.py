final = []

with open ('Working files/Day 1 Calibration.txt') as file:
    for line in file:
        numbers = []
        for c in line:
            if c.isdigit(): numbers.append(c)
        count = len(numbers)
        first = numbers[0] #We know all of these have at least one number, but some don't have two.
        second = numbers[count - 1]
        linevalue = int(first + second)
        final.append(linevalue)
print(sum(final))
