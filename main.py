import os
from tkinter import Y


'''
This is my game of Black Jack. I am doing this for my coding course capstone project. My goal is to create a fully flushed out and 
interactive game of Black Jack - but I will start with the basics and add functionality as I continue.

The code will be brutish and not very clean. I am still learning python and will continue to get better - this is my first attempt!

Feel free to add onto the code and make the game unique and your own. I did the best I could to make the code easy and readable!

I hope you enjoy my game of Black Jack!  
'''

# This function is used to give the rules of Black Jack. It will be used every time the player chooses to see the rules of black jack again
from configparser import MAX_INTERPOLATION_DEPTH
from sre_constants import CATEGORY_DIGIT

from card import Card
from house import House


def rules_of_black_jack():
    print("The rules of Black Jack are as follows:\n")
    print("1) You will be give 2 cards facing up. The value of the cards are as follows:")
    print("    1.1) Any numbered card will be worth the cards value")
    print("    1.2) Any face card will be worth 10")
    print("    1.3) The Ace will be worth either 11 or 1 depending on your choice!")
    print("2) The dealer will one card face up and one card face down")
    print("3) You can choose to recieve cards (called 'Hit me') or stay (called 'Stay') based on the goal of 21")
    print("4) The goal of Black Jack is to get cards toatalling in value 21. If you go over you bust. Whoever is closer to 21 (but not bust) winst the game \n")

'''
Introduction of the game
'''

print("Welcome to the Milind Casino \n")
rules_of_black_jack()

'''
Start of the game
'''

# THIS IS THE MAIN PART OF THE GAME. 
while True:
    # CREATING THE DECK OF CARDS. THERE IS BOTH A LIST REPRESENTATION AND DICTIONARY REPRESENTATION OF THE DECK. THEY WILL BE NAMED ACCORDINGLY
    card = Card()
    deck_list = card.create_deck_list() # DECK IN LIST FORM
    deck_dict = card.create_deck_dict(deck_list) # DECK IN DICTIONARY FORM

    # CHECKING IF THE USER WANTS TO PLAY THE GAME
    continue_var = input("\nWould you like to play? Enter yes [Y] or no [N]: ").strip().lower()
    if (continue_var == "n"):
        break
    else:

        # THIS IS GETTING THE TWO INITIAL CARDS FOR THE HOUSE
        house_player = House()
        house_init_tuple = house_player.house_initial(deck_dict)

        # THIS IS USED TO CLEAR THE CONSOLE FOR A MORE CLEAN LOOKING GAME 
        clear = lambda: os.system('clear')
        clear()

        # FETCHING AND SHOWING THE CURRENT CARDS OF THE HOUSE
        print("HOUSES CARDS: ")
        for card_ in house_init_tuple:
            new_dict = {card : deck_dict[card_]}
            temp_list = card_.split("_")
            suite = temp_list[2]
            card.card_representation(deck_dict[card_], suite[0], deck_dict[card_])
        
        # DELETING THE CARDS THE HOUSE GOT FROM THE DICTIONARY
        for card in house_init_tuple:
            del deck_dict[card]

        # FETCHING AND SHOWING THE CURRENT CARDS OF YOU, THE PLAYER
        
            
        

    





 