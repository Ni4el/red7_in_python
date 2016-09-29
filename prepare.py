from itertools import product
from random import shuffle
from operator import itemgetter
import sys



class Prepare:

    global player_hand1, player_hand2, player_hand3, player_hand4, palette1, palette2, palette3, palette4, CANVAS, paletts, deck
    player_hand1 = []
    player_hand2 = []
    player_hand3 = []
    player_hand4 = []
    palette1 = []
    palette2 = []
    palette3 = []
    palette4 = []
    CANVAS = []
    deck = []
    paletts = palette1 + palette2 + palette3 + palette4

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
        cards_count = palette * players

        for i in range(cards_count):
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
        print("*****************")
        print("player_hand2")
        print(player_hand2)
        print(palette2)
        print("*****************")
        print("player_hand3")
        print(player_hand3)
        print(palette3)
        print("*****************")
        print("player_hand4")
        print(player_hand4)
        print(palette4)
        print("*****************")

        return deck


    """Verify cards on each paletts with number and color"""
    def verify_winner():

        same_values = []
        paletts = palette1 + palette2 + palette3 + palette4
        # paletts = [(4, '3Blue'), (4, '4Green'), (4, '7Red'), (2, '6Orange')]

        # verify which card has the higest number
        winner1 = max(paletts, key=itemgetter(0))

        # verify which card has the higest color
        for j in range(len(paletts)):
            if paletts[j][0] == winner1[0]:
                same_values.append(paletts[j])
                print("same value")
                print(same_values)
                print(len(same_values))

        if len(same_values) > 1:
            winner2 = max(same_values, key=itemgetter(1))
        else:
            winner2 = winner1

        # verify wich player has the higest card
        winner_player = paletts.index(winner2) + 1

        print(paletts)
        print("----")
        print(winner2)
        print("----")
        print(winner_player)

        return winner_player




    def next_player(players, winner_player):

        if players > winner_player:
            next_player = winner_player + 1
        else:
            next_player = 1

        hand = globals()['player_hand%s' % next_player]
        palette = globals()['palette%s' % next_player]

        return next_player, hand, palette


    def add_card(hand, palette, pal = True, both = False):

            wrong_number = "Nie masz takiej karty"

            if pal:
                text = "do palety"
                card = palette
            else:
                text = "na tło"
                card = CANVAS

            number = input("Którą kartę chcesz zagrać z ręki "+text+" (numer karty): ")
            if int(number) not in range(1, 7):
                print(number)
                print(wrong_number)

            color_number = input("Którą kartę chcesz zagrać z ręki "+text+" (numer koloru): ")
            if int(color_number) not in range(1, 7):
                print(wrong_number)


            for i in hand:
                if int(number) == i[0]:
                    if color_number == i[1][:1]:
                        card.append(i)
                        print("wbrana karta")
                        print(i)
                        hand.remove(i)

            print("ręka")
            print(hand)
            print("paleta")
            print(palette)
            print("Canvas")
            print(CANVAS)

            if both == True:
                return Prepare.add_card(hand, palette, False, False)



    def verify_rule():

        print("Canvas")
        print(CANVAS[-1])

        actual_rule = CANVAS[-1][1]
        Prepare.f(actual_rule)

    """Function used like switch in another programming language"""
    def f(x):
        return {
            'a': 1,
            'b': 2,
        }[x]
    # }.get(x, 9)    # 9 is default if x not found










