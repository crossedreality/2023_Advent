#https://docs.python.org/3/howto/sorting.html
from collections import Counter
from operator import attrgetter

#region
CARDSTR = {
    "2":"02",
    "3":"03",
    "4":"04",
    "5":"05",
    "6":"06",
    "7":"07",
    "8":"08",
    "9":"09",
    "T":"10",
    "J":"11",
    "Q":"12",
    "K":"13",
    "A":"14"
 }
#endregion

#region Classes
class Hand:
    def __init__(self, cards, bid):
        self.cards = [CARDSTR[c] for c in cards]
        self.high = ''.join(self.cards)
        self.bid = int(bid)
        self.type = self.gettype()
    
    def gettype(self):
        unique = Counter(self.cards).values()
        if 5 in unique: return 7 #Five of a kind
        elif 4 in unique: return 6 #Four of a kind
        elif 3 in unique:
            if 2 in unique: return 5 #Full house
            else: return 4 #Three of a kind
        elif 2 in unique:
            if Counter(unique)[2] == 2: return 3 #Two pair
            else: return 2 #One pair
        else: return 1 #High card
    
    def getwin(self, rank):
        return self.bid * rank
#endregion
hands = []
winnings = []
with open ('Working files/Day 7 Data.txt') as file:
    for line in file:
        t = line.split()
        hands.append(Hand(t[0],t[1]))

hands.sort(key= attrgetter('type','high'))
for i, hand in enumerate(hands, start=1):
    winnings.append(hand.getwin(i))

print(sum(winnings))