from welcome import welcome
from farewell import farewell
from games import *


def main():
    welcome()

    game_selection = int(input("Please select a game from 1 to 3: "))

    if game_selection == 1:
        play_game_one()
    elif game_selection == 2:
        play_game_two()
    else:
        play_game_three()

    farewell()


if __name__ == "__main__":
    main()

