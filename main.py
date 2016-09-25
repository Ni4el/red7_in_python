#!/usr/bin/python

from prepare import Prepare


def hello():
    print("Witajcie w Red7 \n ************")
    players = input("Proszę podać ilu będzie graczy ")

    if  4 >= int(players) >= 2:

        # player1 = input("Podaj imię pierwszego gracza: ")
        # player2 = input("Podaj imię drugiego gracza: ")
        #
        # if int(players) == 3:
        #     player3 = input("Podaj imię trzeciego gracza: ")
        # elif int(players) == 4:
        #     player3 = input("Podaj imię trzeciego gracza: ")
        #     player4 = input("Podaj imię czwartego gracza: ")

        Prepare.generate_array_cards(int(players))
        print("A więc grajmy!")
    elif int(players) == 1:
        print("Troche nas za mało do gry :(")
    else:
        print("To chyba nie jest ilosc graczy :(")



hello();
