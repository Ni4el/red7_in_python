from itertools import product
from random import shuffle

class Prepare:

    """ Generate start deck"""
    def generate_array_cards(players):

        # make a deck of cards
        deck = list(product(range(0, 7), ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indygo', 'Purple']))

        # shuffle the cards
        shuffle(deck)

        player_hand1 = []
        player_hand2 = []
        player_hand3 = []
        player_hand4 = []
        # print(deck)
        # draw seven cards
        palette = 7
        amount_players = palette * players
        print(amount_players)
        for i in range(amount_players):

            # print(deck[i][0], "of", deck[i][1])
            if i <= 6:
                player_hand1.append(deck[i])
            elif 14 > i > 6:
                player_hand2.append(deck[i])
            elif 21 > i > 13:
                player_hand3.append(deck[i])
            elif 28 > i > 20:
                player_hand4.append(deck[i])
            print(deck)
            del deck[i]
        print("player_hand1")
        print(player_hand1)
        print("player_hand2")
        print(player_hand2)
        print("player_hand3")
        print(player_hand3)
        print("player_hand4")
        print(player_hand4)
        print(len(deck))




