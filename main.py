#!/usr/bin/python

from prepare import Prepare

# global players

class Helper:
    players = 0

def hello():
    print("Witajcie w Red7 \n ************")
    players = input("Proszę podać ilu będzie graczy ")
    players = int(players)

    Helper.players = players
    # for i in range(100):
    #     print(i)

    # if 4 >= int(players) >= 2:

        # player1 = input("Podaj imię pierwszego gracza: ")
        # player2 = input("Podaj imię drugiego gracza: ")
        #
        # if int(players) == 3:
        #     player3 = input("Podaj imię trzeciego gracza: ")
        # elif int(players) == 4:
        #     player3 = input("Podaj imię trzeciego gracza: ")
        #     player4 = input("Podaj imię czwartego gracza: ")

    if Prepare.generate_start_cards(players):
        Prepare.verify_rule()

    #     print("A więc grajmy!")
    # elif int(players) == 1:
    #     print("Troche nas za mało do gry :(")
    # else:
    #     print("To chyba nie jest ilosc graczy :(")



def move(deck):

    winner_player = Prepare.verify_winner()
    next_player, hand, palette = Prepare.next_player(Helper.players, winner_player)


    print('Następny jest gracz ' + str(next_player))
    print("Na ręce:")
    print(hand)
    print("W palecie")
    print(palette)
    option = input("Co zagrywasz? \n"
                 "1. Kartę na tło \n"
                 "2. Kartę na paletę \n"
                 "3. Kartę na paletę i tło \n"
                 "4. Poddaje się \n")

    if option == "1":
        Prepare.add_card(hand, palette, False, False)
    elif option == "2":
        Prepare.add_card(hand, palette, True, False)
    elif option == "3":
        Prepare.add_card(hand, palette, True, True)
    elif option == "4":
        print("Przegrałeś")
    else:
        print("Wrong number")

    verify_rule = Prepare.verify_rule()
    # verify_cards = Prepare.verify_winner()
    # if verify_cards is True:
    #     Prepare.next_player(players, winner_player)


# def game():
#     deck = hello()
#     # move(deck);
#
# game()
hello()