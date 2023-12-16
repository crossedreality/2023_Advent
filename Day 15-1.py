with open ('Working files/Day 15 Data.txt') as file:
    values = []
    steps = file.read().strip().split(',')
    for step in steps:
        cv = 0
        for c in step:
            cv += ord(c)
            cv *= 17
            cv %= 256
        values.append(cv)
    print(sum(values))