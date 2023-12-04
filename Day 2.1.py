import re #fuck you Kenny

#Define classes
class Game:
    def __init__(self, id):
        self.pulls = []
        self.id = int(id)
        self.possible = True

    def addPull(self, pull):
        self.pulls.append(pull)

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

def pull_possible(pull):
    rlimit = 12
    blimit = 14
    glimit = 13
    if pull.red <= rlimit and pull.blue <= blimit and pull.green <= glimit: return True
    else: return False

#Main program
possible_games = []

with open ('Working files/Day 2 Calibration.txt') as file:
    for line in file:
        gtxt = line.partition(':')
        game = Game(re.search("\d+", gtxt[0]).group())
        pulls = gtxt[2].split(';')
        for pull in pulls:
            pull = pull_parser(pull)
            game.addPull(pull) #I think we'll need these later today.
            if not pull_possible(pull): game.possible = False
        if game.possible: possible_games.append(game)

print(sum(game.id for game in possible_games))
