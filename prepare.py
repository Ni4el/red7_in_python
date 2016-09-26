from itertools import product
from random import shuffle
from operator import itemgetter
import sys

class Prepare:

    global player_hand1, player_hand2, player_hand3, player_hand4, palette1, palette2, palette3, palette4
    player_hand1 = []
    player_hand2 = []
    player_hand3 = []
    player_hand4 = []
    palette1 = []
    palette2 = []
    palette3 = []
    palette4 = []

    """ Generate start deck

        Generate cards for each player hand

        Generate one card to each palette
    """
    def generate_start_cards(players):

        # make a deck of cards
        deck = list(product(range(0, 7), ['7Red', '6Orange', '5Yellow', '4Green', '3Blue', '2Indygo', '1Purple']))
        # deck = list(product(range(0, 7), range(0, 7)))

        # shuffle the cards
        shuffle(deck)
        # sys.exit(deck)

        # draw seven cards
        palette = 7
        amount_players = palette * players

        for i in range(amount_players):
            # print(deck[0][0], "of", deck[0][1])
            if i < 7:
                player_hand1.append(deck[0])
                if i == 6:
                    palette1.append(deck[0])
                    del deck[0]
            elif 14 > i > 6:
                player_hand2.append(deck[0])
                if i == 13:
                    palette2.append(deck[0])
                    del deck[0]
            elif 21 > i > 13:
                player_hand3.append(deck[0])
                if i == 20:
                    palette3.append(deck[0])
                    del deck[0]
            elif 28 > i > 20:
                player_hand4.append(deck[0])
                if i == 27:
                    palette4.append(deck[0])
                    del deck[0]
            del deck[0]


        print("player_hand1")
        print(player_hand1)
        print(palette1)
        print("player_hand2")
        print(player_hand2)
        print(palette2)
        print("player_hand3")
        print(player_hand3)
        print(palette3)
        print("player_hand4")
        print(player_hand4)
        print(palette4)
        print(len(deck))
        Prepare.verify_winner()

    def verify_winner():

        test = []
        same_values = []
        test = palette1 + palette2 + palette3 + palette4

        winner1 = max(test,key=itemgetter(0))[0]

        winner2 = []

        print(type(test))
        print("---2323-")
        for j in range(len(test)):
            if test[j][0] == winner1:

                same_values = test[j];
                print(same_values)

        print(type(same_values))
        winner2 = max(list(same_values), key=itemgetter(1))


        # print(test)
        # print("----")
        # print(winner1)
        # print("----")
        # print(d[winner1])







