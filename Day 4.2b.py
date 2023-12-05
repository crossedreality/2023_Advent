import re

#region Classes
class Card:
    def __init__(self, id, winning_numbers, card_numbers):
        self.id = int(id)
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
        self.instances = 1
    
    def cardvalue(self):
        matches = 0
        for value in self.card_numbers:
            if value in self.winning_numbers: 
                matches += 1
        return matches
#endregion

#region Functions
def cardcloner(cards, card, value):
    for wins in range(1,value + 1):
        prize = findcard(cards, card.id + wins)
        if prize: prize.instances += 1

def findcard(cards, id):
    return next((card for card in cards if card.id == id), None)
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
    
    for card in cards:
        print(f"Card: {card.id} Instances: {card.instances}")
        for _ in range(card.instances):
            value = card.cardvalue()
            if value > 0: cardcloner(cards, card, value)

print(sum(card.instances for card in cards))
