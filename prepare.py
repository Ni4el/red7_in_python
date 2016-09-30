#!/usr/bin/python

from itertools import product
from random import shuffle
from operator import itemgetter
import sys

class Helper:
    players = 2
    canvas = []
    deck = []
    for i in range(1,5):
        globals()['player_hand%s' % i] = []
        globals()['palette%s' % i] = []


class Prepare:

    """ Generate start deck

        Generate cards for each player hand

        Generate one card to each palette
    """
    def generate_start_cards(players):
        Helper.players = players

        # make a deck of cards
        deck = list(product(range(1, 8), ['7Red', '6Orange', '5Yellow', '4Green', '3Blue', '2Indigo', '1Violet']))
        # deck = list(product(range(0, 7), range(0, 7)))

        # shuffle the cards
        shuffle(deck)
        # print(len(deck))
        # sys.exit(deck)

        # draw seven cards
        count = 1
        start_deck = 7
        cards_count = start_deck * players


        for i in range(cards_count):
            # print(deck[0][0], "of", deck[0][1])
            if i % 7 == 0:
                player_hand = globals()['player_hand%s' % count]
                front = globals()['palette%s' % count]
                count += 1
                front.append(deck[1])
                del deck[1]
                player_hand.append(deck[0])
            else:
                player_hand.append(deck[0])

            del deck[0]

        Helper.deck = deck

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
        print(len(deck))
        if len(deck) == 49-cards_count-players:
            return True


    def next_player(PLAYERS, winner_player):

        if PLAYERS > winner_player:
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
                card = canvas

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

        canvas = ('1Violet')
        # canvas = Helper.canvas[1]
        print("Canvas")
        print(canvas)

        if bool(canvas):
            if canvas == '7Red':
                Prepare.rule_the_higest()
            elif canvas == '6Orange':
                Prepare.rule_the_higest()
            elif canvas == '5Yellow':
                Prepare.rule_the_higest()
            elif canvas == '4Green':
                Prepare.rule_the_higest()
            elif canvas == '3Blue':
                Prepare.rule_the_higest()
            elif canvas == '2Indigo':
                Prepare.rule_the_higest()
            elif canvas == '1Violet':
                Prepare.rule_below_4()
            else:
                "Error"
        else:
            Prepare.rule_the_higest()



    """Rule 7: paletts with the higest card"""

    def rule_the_higest():

        winners = []
        # verify which card has the higest color
        for j in range(1, Helper.players+1):
            player_hand = globals()['player_hand%s' % j]
            winners.append(max(player_hand, key=itemgetter(0,1)))
            # print("kolejka")
            # print(player_hand)
            # print(winners)

        return winners.index(max(winners, key=itemgetter(0, 1)))+1

    """Rule 1: most cards below 4"""

    def rule_below_4():

        winners = []

        for j in range(1, Helper.players + 1):
            player_hand = globals()['player_hand%s' % j]

            for k in player_hand:
                # if player_hand[i][0] < 3:
                #     winners.append(player_hand[j])

                print("kolejka")
                print(player_hand[k])
            print("")

        # return winners.index(max(winners, key=itemgetter(0, 1))) + 1

