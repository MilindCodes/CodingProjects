import random

'''
This is the house class for my Black Jack project.

The goal of this class is to create a bot that acts as the house in the following ways:
1. If the value of the cards held by the bot are below 17, it draws another card
2. If the value of the cards held by the bot are above 17, it stays
'''

class House():

    def __init__(self) -> None:
        pass

    def house_initial(self, deck) -> tuple:
        if not(type(deck) == dict):
            raise Exception("INPUT MUST BE A DICTIONARY")
        card_one = random.choice(list(deck))
        card_two = random.choice(list(deck))
        while card_two == card_one:
            card_two = random.choice(list(deck))
        return card_one, card_two

    def hit_or_pass(self, *args, deck) -> str:
        if sum(args) <= 17:
            new_card = random.choice(list(deck))
            return new_card, new_card.values()
        else:
            return "STAY"
        