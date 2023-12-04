import re #fuck you Kenny

#Define classes
class Game:
    def __init__(self, id):
        self.pulls = []
        self.id = int(id)
        self.possible = True
        self.mRed = 0
        self.mGreen = 0
        self.mBlue = 0

    def addPull(self, pull):
        self.pulls.append(pull)
        self.mRed = max(pull.red, self.mRed)
        self.mGreen = max(pull.green, self.mGreen)
        self.mBlue = max(pull.blue, self.mBlue)
    
    def power(self):
        return self.mRed * self.mGreen * self.mBlue

class Pull:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

#Define functions
def pull_parser(pull):
    red = 0
    blue = 0
    green = 0
    parse = pull.split(',')
    for p in parse:
        if "red" in p: red = int(re.search("\d+", p).group())
        elif "blue" in p: blue = int(re.search("\d+", p).group())
        elif "green" in p: green = int(re.search("\d+", p).group())
    return Pull(red,green,blue)

#Main program
games = []

with open ('Working files/Day 2 Calibration.txt') as file:
    for line in file:
        gtxt = line.partition(':')
        game = Game(re.search("\d+", gtxt[0]).group())
        pulls = gtxt[2].split(';')
        for pull in pulls:
            pull = pull_parser(pull)
            game.addPull(pull) 
        games.append(game)
        print(game.power())

print(sum(game.power() for game in games))
