# 12/01/2022
# First Python Project - Rock Paper Scissor Game (v1)

# Modules to be used in the game.
import random
import math
from colorama import Fore, Style

# Functions I used in the game.
def ult(text):      # Underlined Text
    underl_text = "\x1B[4m" + text + "\x1B[0m"
    return underl_text

def redt(text):     # Red Text
    redt_text = Fore.RED + text + Style.RESET_ALL
    return redt_text

def grt(text):      # Green Text
    grt_text = Fore.GREEN + text + Style.RESET_ALL
    return grt_text

# Welcoming the user.
player_name = input("What's your name? ")
print(f"Hi, {player_name}! Welcome to 'Rock Paper Scissors' game!")

# Setting up the variables.
possible_moves = ['Rock', 'Paper', 'Scissors']
continue_choice = ['Y', 'N']
comp_wins = 0
player_wins = 0
num_round = 0
num_tie = 0

# Looping the main game.
game_running = True

while game_running:

    comp_choice = random.choice(possible_moves)
    player_choice = None
    continue_game = None
    num_round += 1
    print(Fore.BLUE + f'\nRound {num_round}' + Style.RESET_ALL)

    while player_choice not in possible_moves:
        ask_player = 'Pick a move for this round. Rock, Paper, or Scissors: '
        player_choice = str(input(f'{ask_player}')).capitalize()

        if player_choice in set(possible_moves):
            break
        print(redt('Invalid input. Please try again!'))

    print(f'{player_name}: {player_choice}')
    print(f'Computer: {comp_choice}\n')

    if player_choice == comp_choice:
        print(ult("It's a tie! No one wins, and no one loses this round."))
        num_tie += 1

    elif player_choice == 'Rock' and comp_choice == 'Scissors':
        print(ult(f'{player_name} wins!'))
        player_wins += 1

    elif player_choice == 'Scissors'and comp_choice == 'Paper':
        print(ult(f'{player_name} wins!'))
        player_wins += 1

    elif player_choice == 'Paper' and comp_choice == 'Rock':
        print(ult(f'{player_name} wins!'))
        player_wins += 1

    else:
        print(ult('Computer wins!'))
        comp_wins += 1

    while continue_game not in continue_choice:
        continue_game = str(input('Would you like to play again? (Y/N): ')).upper()

        if continue_game == 'N':
            game_running = False

        elif continue_game != 'Y':
            print(redt("Please enter 'Y' for Yes or 'N' for No."))

total_n_tie = num_round - num_tie
det_winner = math.ceil(total_n_tie/2)

# Grammar rules.
time_p = "times"
time_c = "times"
round_ = "rounds"
if player_wins == 1:
    time_p = "time"
if comp_wins == 1:
    time_c = "time"
if total_n_tie == 1:
    round_ = "round"

# Displaying the the results of the game.
print('\n======================================================================\n')
print(f'You have won {player_wins} {time_p} while the computer has won {comp_wins} {time_c}.')
print(f'The number of rounds where there is a tie is {num_tie}. (Not counted/included)')

if comp_wins == player_wins:
    print(grt('\nIt is a tie! Everyone got the same number of wins.'))
    print(grt('Thanks for playing!'))

elif det_winner <= player_wins:
    print(grt(f'\nCongratulations! You have won the best of {total_n_tie} {round_}!'))
    print(grt('Thanks for playing!'))

elif det_winner <= comp_wins:
    print(grt(f'\nUnfortunately, the computer has won the best of {total_n_tie} {round_}.'))
    print(grt('Better luck next time and Thanks for playing!'))
