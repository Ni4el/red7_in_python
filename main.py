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
        move()

    #     print("A więc grajmy!")
    # elif int(players) == 1:
    #     print("Troche nas za mało do gry :(")
    # else:
    #     print("To chyba nie jest ilosc graczy :(")



def move():

    winner_player = Prepare.verify_rule()
    next_player, hand, palette = Prepare.next_player(Helper.players, winner_player)

    if winner_player != next_player:

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
            result = Prepare.add_card(hand, palette, False, False)
        elif option == "2":
            result = Prepare.add_card(hand, palette, True, False)
        elif option == "3":
            result = Prepare.add_card(hand, palette, True, True)
        elif option == "4":
            print("Przegrałeś")
            result = False
        else:
            print("Wrong number")
            result = False

        if result:
            move()
        else:
            print("Nadal przegrywasz")

    else:
        print("Nadal przegrywasz")


hello()