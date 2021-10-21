import random
from colorama import Fore
import datetime


# -----------------FUNCTIONS-----------------------

def show_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] == "O":
                print(Fore.RED + "O", end=" ")
            elif game[i][j] == "X":
                print(Fore.BLUE + "X", end=" ")
            else:
                print(Fore.YELLOW + "-", end=" ")
        print(Fore.RESET)


def check(user, starting_time):
    str = game[0][0] + game[1][1] + game[2][2] + " " + game[0][2] + game[1][1] + game[2][0]
    for i in range(3):
        str += " " + game[i][0] + game[i][1] + game[i][2] + " " + game[0][i] + game[1][i] + game[2][i]
    if "XXX" in str:
        print("Player 1 wins.")
        print("Game time elapsed: ", datetime.datetime.now() - starting_time)
        exit()
    elif "OOO" in str:
        if user == "p2":
            print("Player 2 wins.")
        else:
            print("computer wins.")
        print("Game time elapsed:", datetime.datetime.now() - starting_time)
        exit()

def play_with_player2(starting_time):
    Number_of_game_moves = 9
    while True:
        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "X"
                    break
                else:
                    print("this cell is not empty.")
            else:
                print("row or col is invalid. ")
        show_board()
        check("p2", starting_time)
        if Number_of_game_moves == 1:
            print("There is no winner and result is draw.")
            print("Game time elapsed: ", datetime.datetime.now() - starting_time)
            break
        Number_of_game_moves -= 2

        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "O"
                    break
                else:
                    print("row or col is invalid. ")
            else:
                print("row or col is invalid. ")
        show_board()
        check("p2", starting_time)


def play_with_computer(starting_time):
    Number_of_game_moves = 9
    while True:
        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "X"
                    break
                else:
                    print("this cell is not empty.")
            else:
                print("row or col is invalid. ")
        show_board()
        check("pc", starting_time)
        print("-----------------")
        if Number_of_game_moves == 1:
            print("There is no winner and result is draw.")
            print("Game time elapsed: ", datetime.datetime.now() - starting_time)
            break
        Number_of_game_moves -= 2

        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if row in range(0, 3) and col in range(0, 3):
                if game[row][col] == "-":
                    game[row][col] = "O"
                    break
        show_board()
        check("pc", starting_time)


#------------------main----------------------

game = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

show_board()

choice = input("If you want to play with computer press 1 and if you want to play with player 2 press 2 : ")
if choice == "2":
    starting_time = datetime.datetime.now()
    play_with_player2(starting_time)
elif choice == "1":
    starting_time = datetime.datetime.now()
    play_with_computer(starting_time)

