#!/usr/bin/python

from prepare import Prepare

global players

players = 0

def hello():
    print("Witajcie w Red7 \n ************")
    players = input("Proszę podać ilu będzie graczy ")


    # for i in range(100):
    #     print(i)


    if  4 >= int(players) >= 2:

        # player1 = input("Podaj imię pierwszego gracza: ")
        # player2 = input("Podaj imię drugiego gracza: ")
        #
        # if int(players) == 3:
        #     player3 = input("Podaj imię trzeciego gracza: ")
        # elif int(players) == 4:
        #     player3 = input("Podaj imię trzeciego gracza: ")
        #     player4 = input("Podaj imię czwartego gracza: ")

        deck = Prepare.generate_start_cards(int(players))

    #     print("A więc grajmy!")
    # elif int(players) == 1:
    #     print("Troche nas za mało do gry :(")
    # else:
    #     print("To chyba nie jest ilosc graczy :(")
        return deck


def move(deck):

    winner_player = Prepare.verify_winner()
    next_player, hand, palette = Prepare.next_player(players, winner_player)


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
        print("1")
    elif option == "2":
        Prepare.add_card_to_palette(hand, palette, deck)
    elif option == "3":
        print("3")
    elif option == "4":
        print("4")
    else:
        print("Wrong number")




def game():

    deck = hello()
    move(deck);



game()