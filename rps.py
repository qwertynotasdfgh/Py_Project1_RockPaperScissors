import random

# Game code:
def game():
    # Computers choices:
    item_choices = ["rock", "paper", "scissors"]
    # Scores
    comp_score = 0
    player_score = 0
    # Game logic:
    while comp_score < 3 and player_score < 3:
        computer_choice = random.choice(item_choices)
        player_choice = input("Choose 'ROCK', 'PAPER' OR 'SCISSORS'\n")
        if player_choice.lower() == computer_choice:
            print("Draw! \nRun it back!\n")
        elif player_choice.lower() == 'rock' and computer_choice == 'paper':
            print("Computer chose paper, it gained 1 point\n")
            comp_score += 1
            print(f"The score is now PLAYER:{player_score} COMPUTER:{comp_score}\n")
        elif player_choice.lower() == 'rock' and computer_choice == 'scissors':
            print("Computer chose scissors, you gained 1 point\n")
            player_score += 1
            print(f"The score is now PLAYER:{player_score} COMPUTER:{comp_score}\n")
        elif player_choice.lower() == 'paper' and computer_choice == 'rock':
            print("Computer chose rock, you gained 1 point\n")
            player_score += 1
            print(f"The score is now PLAYER:{player_score} COMPUTER:{comp_score}\n")
        elif player_choice.lower() == 'paper' and computer_choice == 'scissors':
            print("Computer chose scissors, it gained 1 point\n")
            comp_score += 1
            print(f"The score is now PLAYER:{player_score} COMPUTER:{comp_score}\n")
        elif player_choice.lower() == 'scissors' and computer_choice == 'paper':
            print("Computer chose paper, you gained 1 point\n")
            player_score += 1
            print(f"The score is now PLAYER:{player_score} COMPUTER:{comp_score}\n")
        elif player_choice.lower() == 'scissors' and computer_choice == 'rock':
            print("Computer chose rock, it gained 1 point\n")
            comp_score += 1
            print(f"The score is now PLAYER:{player_score} COMPUTER:{comp_score}\n")
        else:
            print("Please choose either rock, paper or scissors. If you did and the game didn't work please double check your spelling\n")
    # End game messages:
    if player_score == 3:
        print(f"You beat the computer {player_score} to {comp_score}")
    elif comp_score == 3:
        print(f"Computer won {comp_score} to {player_score}")
    else:
        print("Error")
    


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