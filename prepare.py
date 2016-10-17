#!/usr/bin/python

from itertools import product
from random import shuffle
from operator import itemgetter
from collections import Counter

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
        print("###########################")

        """Check if correct number of card in deck"""
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
                card = Helper.canvas

            number = input("Którą kartę chcesz zagrać z ręki "+text+" (numer karty): ")
            if int(number) not in range(1, 7):
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

            if both == True:
                return Prepare.add_card(hand, palette, False, False)
            else:
               return True

    def verify_rule():

        result = 0
        #canvas = ('1Violet')
        canvas = Helper.canvas
        print("Canvas")
        print(canvas)

        if bool(canvas):
            canvas = canvas[-1]
            if canvas == '7Red':
                result = Prepare.rule_the_higest()
            elif canvas == '6Orange':
                result = Prepare.rule_one_number()
            elif canvas == '5Yellow':
                result = Prepare.rule_one_color()
            elif canvas == '4Green':
                result = Prepare.rule_even_cards()
            elif canvas == '3Blue':
                result = Prepare.rule_diffrent_colors()
            elif canvas == '2Indigo':
                result = Prepare.rule_cards_that_form_run()
            elif canvas == '1Violet':
                result = Prepare.rule_below_4()
            else:
                "Error"
        else:
            result = Prepare.rule_the_higest()


        print("result")
        print(result)
        return result


    """Rule 1: most cards below 4"""

    def rule_below_4():

        winners = []
        compatible = []

        #invoke to players paletts
        for j in range(1, Helper.players + 1):
            palette = globals()['palette%s' % j]
            #find cards below 4, count, and assign to common list winners
            for i in range(len(palette)):
                if palette[i][0] < 4:
                    compatible.append(palette[i])
            # print(player_hand)
            winners.append((len(compatible), max(compatible, key=itemgetter(0, 1))))

            compatible = []

        return winners.index(max(winners, key=itemgetter(0, 1))) + 1

    """Rule 2: CARDS THAT FORM A RUN """

    def rule_cards_that_form_run():

        sequence = []
        sequences = {}
        card = 0
        l = 1
        # verify which card has the higest color
        for j in range(1, Helper.players+1):
            palette = globals()['palette%s' % j]
            sorted_palette = sorted(palette, key=itemgetter(0))
            for i in range(len(sorted_palette) + 1):
                if i == 0:
                    card = sorted_palette[i][0]
                elif i == 7:
                    sequence.append([l, card])
                    l = 1
                else:
                    if sorted_palette[i][0] == (card + 1):
                        card = sorted_palette[i][0]
                        l += 1
                    else:
                        sequence.append([l, card])
                        card = sorted_palette[i][0]
                        l = 1

            # save the higest sequence of card
            sequences["player{0}".format(j)] = max(sequence, key=itemgetter(0, 1))
            # print("ręka")
            # print(sorted_palette)
            # print("sekwencja")
            # print(sequence)
            sequence = []
        # verify which player has the longes sequence
        winners = max(sequences.values(), key=itemgetter(0, 1))

        winner = list(sequences.keys())[list(sequences.values()).index(winners)]
        winner = winner[-1]

        # print("kozak")
        # print(sequences)
        # print(winners)
        """SPR. gdy dwóch graczy ma taka sama sekwencje i najwyzsza karte"""

        return winner

    """Rule 3: cards of all diffrent colors"""

    def rule_diffrent_colors():

        winners = []
        compatible = []
        cards = []

        # invoke to players paletts
        for j in range(1, Helper.players + 1):
            palette = globals()['palette%s' % j]
            # find cards below 4, count, and assign to common list winners
            # print(palette)
            for i in range(len(palette)):
                if palette[i][1] not in compatible:
                    compatible.append(palette[i][1])

            # print("%%%%%%%")
            # print(compatible)
            cards.append([len(compatible), max(compatible)])
            compatible = []
        # print("^%^%^%$^$%")
        # print(cards)
        return cards.index(max(cards, key=itemgetter(0, 1))) + 1

    """Rule 4: most even cards"""

    def rule_even_cards():

        winners = []
        compatible = []
        cards = []

        # invoke to players paletts
        for j in range(1, Helper.players + 1):
            palette = globals()['palette%s' % j]
            # find cards below 4, count, and assign to common list winners
            for i in range(len(palette)):
                if (palette[i][0] % 2) == 0:
                    compatible.append(palette[i])

            winners.append((len(compatible), max(compatible, key=itemgetter(0, 1))))
            compatible = []
        # print("^%^%^%$^$%")
        # print(winners)
        return winners.index(max(winners, key=itemgetter(0, 1))) + 1

    """Rule 5: cards of one color

        summary: list(the longest sequence, color, the higest number)

        return
        number of player who wins
    """

    def rule_one_color():

        winners = []
        compatible = []
        cards = []

        # invoke to players paletts
        for j in range(1, Helper.players + 1):
            palette = globals()['palette%s' % j]
            for i in range(len(palette)):
                compatible.append(palette[i][1])

            print(palette)
            pogrupowane = Counter(compatible)
            colors = max(pogrupowane.items(), key=itemgetter(1, 0))
            print("NAJCZĘSTSZY KOLOR")
            print(colors)
            values = []
            indeksy = [item for item, v in enumerate(palette) if v[1] == colors[0]]
            print("indeksy koloru w tablicy")
            print(indeksy)
            for k in range(len(indeksy)):
                values.append(palette[indeksy[k]])
            winners.append((colors[1], colors[0], max(values, key=itemgetter(0, 1))[0]))
            print(winners)
            compatible = []
            print("^%^%^%$^$%")

        return winners.index(max(winners, key=itemgetter(0, 1, 2))) + 1

    """Rule 6: cards of one number

            summary: list(the longest sequence, color, the higest number)

            return
            number of player who wins
        """

    def rule_one_number():

        winners = []
        compatible = []
        cards = []

        # invoke to players paletts
        for j in range(1, Helper.players + 1):
            palette = globals()['palette%s' % j]
            for i in range(len(palette)):
                compatible.append(palette[i][0])

            print(palette)
            pogrupowane = Counter(compatible)
            print("pogrupowane numery")
            print(pogrupowane)
            colors = max(pogrupowane.items(), key=itemgetter(1, 0))
            print("NAJCZĘSTSZY numer")
            print(colors)

            values = []
            indeksy = [item for item, v in enumerate(palette) if v[0] == colors[0]]
            print("indeksy koloru w tablicy")
            print(indeksy)
            for k in range(len(indeksy)):
                values.append(palette[indeksy[k]])
            winners.append((colors[1], colors[0], max(values, key=itemgetter(0, 1))[1],))
            print(winners)
            compatible = []
            print("^%^%^%$^$%")

        return winners.index(max(winners, key=itemgetter(0, 1, 2))) + 1

    """Rule 7: paletts with the higest card"""

    def rule_the_higest():

        winners = []
        # verify which card has the higest color

        for j in range(1, Helper.players+1):
            palette = globals()['palette%s' % j]
            winners.append(max(palette, key=itemgetter(0, 1)))

        return winners.index(max(winners, key=itemgetter(0, 1))) + 1
