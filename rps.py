import random

# Game code:
def game():
    # Computers choice:
    item_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(item_choices)
    # Scores
    comp_score = 0
    player_score = 0
    # Game logic:
    while comp_score < 3 or player_score < 3:
        player_choice = input("Choose 'ROCK', 'PAPER' OR 'SCISSORS'")
        if player_choice == computer_choice:
            print("Draw! \nRun it back!")
        elif player_choice.lower() == 'rock' and computer_choice == 'paper':
            pass
        elif player_choice.lower() == 'rock' and computer_choice == 'scissors':
            pass
        elif player_choice.lower() == 'paper' and computer_choice == 'rock':
            pass
        elif player_choice.lower() == 'paper' and computer_choice == 'scissors':
            pass
        elif player_choice.lower() == 'scissors' and computer_choice == 'paper':
            pass
        elif player_choice.lower() == 'scissors' and computer_choice == 'rock':
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