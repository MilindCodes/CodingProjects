import random

'''
This is the player class for my Black Jack project.

The purpose of this class is much the same of the house class, except it is meant to be used by the player. 
'''

class Player():

    def __init__(self) -> None:
        pass

    def player_initial(self, deck) -> tuple:

        # THIS MAKES SURE THAT THE VALUE PASSED TO THIS METHOD IS A DICTIONARY. IF IT IS NOT THE CODE WILL NOT WORK
        if not(type(deck) == dict):
            raise Exception("INPUT MUST BE A DICTIONARY")

        # PICKS A CARD AT RANDOM FROM THE PROVIDED DECK. IT WILL ALSO RETURN THE CARDS SO THAT THEY CAN BE REMOVED FROM THE DECK ONCE THEY ARE ADDED TO THE PLAYERS HAND 
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