import re

#region Classes
class Card:
    def __init__(self, id, winning_numbers, card_numbers):
        self.id = id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
    
    def cardvalue(self):
        matches = 0
        for value in self.card_numbers:
            if value in self.winning_numbers: 
                matches += 1
                #print(value)
        return self.cardmather(matches)
    
    def cardmather(self, matches):
        if matches <= 1: return matches
        else:
            v = 1
            for _ in range(matches - 1):
                v *= 2
            return v
#endregion

#Main 
cards = []

with open ('Working files/Day 4 Data.txt') as file:
    for line in file:
        card_text = line.partition(':')
        card_id = re.search("\d+", card_text[0]).group()
        game_numbers = card_text[2].partition('|')
        winning_numbers = game_numbers[0].split()
        card_numbers = game_numbers[2].split()
        cards.append(Card(card_id,winning_numbers,card_numbers))
    
print(sum(card.cardvalue() for card in cards))
