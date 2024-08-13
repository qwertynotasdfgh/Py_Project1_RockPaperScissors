import random

# Game code:
def game():
    pass

# Ask player wether or not the want to play the game:
def do_you_want_to_play():
    while True:
        is_player_playing = input("Would you like to play a game of rock, paper, scissors? type: (Y/N).\n")
        if is_player_playing.lower() == "y":
            game()
            break
        elif is_player_playing.lower() == "n":
            print("Next time then! \nExiting...\n")
            break
        else:
            print("Please enter a valid answer, type 'Y' for yes or 'N' for no.")

# Starting the code:
do_you_want_to_play()