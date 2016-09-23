from random import randint
from random import choice

class Prepare:

    """ Generate start deck"""
    def generate_array_cards():
        cards = {}
        # colors = ["red", "orange", "yellow", "green", "blue", "indygo", "purple"]
        j = 1
        k = 0

        for i in range(49):

            i += 1;
            k += 1;

            # cards[i] = str(k) + colors[j]
            cards[i] = str(k) + str(j)

            if i % 7 == 0:
                j += 1
                k = 0

        # print(cards)
        return cards

    """ Generate cards for each players"""

    def generate_players_cards(players):

        cards = Prepare.generate_array_cards()

        player_hand1 = []
        hands = 1 * 7
        i = 1

        for i in range(hands):
            card = choice(list(cards.keys()))

            print(card)
            print(cards[card])

            player_hand1[i] = cards[card]
            i += 1

            del cards[card]


        print(player_hand1)

        print(cards)

        player_hand1 = []
        player_hand2 = []

        if players == 3:
            player_hand3 = []
        elif players == 4:
            player_hand3 = []
            player_hand4 = []


    # def generate_player_hand():
    #
    #     cards = Prepare.generate_array_cards()

