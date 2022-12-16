# NVC Ungco - 12/15/2022
# First Python Project - Rock Paper Scissor Game (v1.1)

# Modules/Packages used
import sys
from math import ceil
from os import system
from random import choice
from time import sleep
from colorama import Fore, Style


# To reveal text instead of printing it right away
def reveal_text(text):
    for letter in text + '\n':
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.01)


# To make the terminal look clean
def clear():
    system('cls')


def unlt(text):     # Underlined Text
    underlined_text = "\x1B[4m" + text + "\x1B[0m"
    return underlined_text


def redt(text):     # Red Text
    red_text = Fore.RED + text + Style.RESET_ALL
    return red_text


def grt(text):      # Green Text
    green_text = Fore.GREEN + text + Style.RESET_ALL
    return green_text


def rps_game():
    # Clear out the terminal for a clean look
    clear()

    # Ask user for their name
    player_name = str(input("Enter your name: "))
    sleep(1)
    clear()

    # Welcome the user and announce the game in a cool way
    reveal_text(f'Hello there, {grt(player_name)}! Welcome to Rock Paper Scissors!\n')
    sleep(1.5)

    # Tell the user the winning rules of the game and who they will be competing with
    reveal_text('In this game, you will be playing Rock Paper Scissors against a computer.\n')
    sleep(1.5)

    reveal_text('''Winning rules for this game:
    1. Paper covers Rock
    2. Scissors cut Paper
    3. Rock crushes Scissors\n''')
    sleep(3)

    reveal_text("Press enter to continue.")
    input()
    clear()

    comp_wins = 0
    player_wins = 0
    num_round = 0
    num_tie = 0

    game_running = True

    while game_running:

        num_round += 1
        possible_moves = ['Rock', 'Paper', 'Scissors']
        comp_choice = choice(possible_moves)

        reveal_text(Fore.BLUE + f'Round {num_round}' + Style.RESET_ALL)     # Current round
        sleep(1)

        # Ask user for their choice of move
        ask_player = 'Pick a move for this round. Rock, Paper, or Scissors: '
        player_choice = str(input(f'{ask_player}')).capitalize()

        # Make sure user input is valid
        while True:
            if player_choice not in possible_moves:
                print(redt('Invalid input. Please try again!\n'))
                player_choice = str(input(f'{ask_player}')).capitalize()

            elif player_choice in possible_moves:
                break

        clear()
        print(Fore.BLUE + f'Round {num_round}' + Style.RESET_ALL)   # Current round

        # Display the chosen move of user and the computer
        if player_choice == comp_choice:
            reveal_text(f'{player_name} and the computer have both chosen {comp_choice}.\n')
        else:
            reveal_text(
                f"{player_name} chose {player_choice} while Computer chose {comp_choice}.\n"
                )
        sleep(1)

        # Display the result/winner of the round
        if player_choice == comp_choice:
            num_tie += 1
            reveal_text(unlt("It's a tie! No one wins, and no one loses this round.\n"))
            sleep(1)

        if player_choice == 'Rock':
            if comp_choice == 'Scissors':
                player_wins += 1
                reveal_text('Rock crushes Scissors!\n')
                sleep(1)
                reveal_text(unlt(f'{player_name} wins!\n'))
                sleep(1.5)
            elif comp_choice == 'Paper':
                comp_wins += 1
                reveal_text('Paper covers Rock!\n')
                sleep(1)
                reveal_text(unlt('Computer wins!\n'))
                sleep(1.5)

        elif player_choice == 'Paper':
            if comp_choice == 'Rock':
                player_wins += 1
                reveal_text('Paper covers Rock!\n')
                sleep(1)
                reveal_text(unlt(f'{player_name} wins!\n'))
                sleep(1.5)
            elif comp_choice == 'Scissors':
                comp_wins += 1
                reveal_text('Scissors cut Paper!\n')
                sleep(1)
                reveal_text(unlt('Computer wins!\n'))
                sleep(1.5)

        elif player_choice == 'Scissors':
            if comp_choice == 'Paper':
                player_wins += 1
                reveal_text('Scissors cut Paper!\n')
                sleep(1)
                reveal_text(unlt(f'{player_name} wins!\n'))
                sleep(1.5)
            elif comp_choice == 'Rock':
                comp_wins += 1
                reveal_text('Rock crushes Scissors!\n')
                sleep(1)
                reveal_text(unlt('Computer wins!\n'))
                sleep(1.5)

        continue_choice = ['Y', 'N']    # List to validate user input choice
        another_round = None
        continue_message = 'Would you like to play again? (Y/N): '

        # User input validation for a rematch
        while another_round not in continue_choice:
            another_round = str(input(f'{continue_message}')).upper()

            if another_round == 'N':
                game_running = False
                sleep(1.5)
                clear()

            elif another_round != 'Y':
                print(redt("Please enter 'Y' for Yes or 'N' for No.\n"))

        sleep(0.5)
        clear()

    rounds_without_tie = num_round - num_tie
    det_winner = ceil(rounds_without_tie/2)

    # Grammar rules.
    time_p = "times"
    time_c = "times"
    round_ = "rounds"

    if player_wins == 1:
        time_p = "time"

    if comp_wins == 1:
        time_c = "time"

    if rounds_without_tie == 1:
        round_ = "round"

    # Display the overall results of the game
    reveal_text(
        f'You have won {player_wins} {time_p} while the computer has won {comp_wins} {time_c}.'
        )
    reveal_text(f'The number of rounds where there is a tie is {num_tie}. (Not counted/included)')
    sleep(1.5)

    # Display who have won the most rounds throughout the game
    if comp_wins == player_wins:
        reveal_text(grt('\nIt is a tie! \nEveryone got the same number of wins.'))
        sleep(3.5)

    elif det_winner <= player_wins:
        reveal_text(grt(f'\nCongratulations, {player_name}!'))
        sleep(1.5)
        reveal_text(grt(f'You have won the best of {rounds_without_tie} {round_}!'))
        sleep(2.5)

    elif det_winner <= comp_wins:
        reveal_text(grt(
            f'\nUnfortunately, the computer has won the best of {rounds_without_tie} {round_}.'
            ))
        sleep(1.5)
        reveal_text(grt('Better luck next time!'))
        sleep(2.5)

    reveal_text("\nPress enter to leave.")
    input()
    clear()

    # Ask the user if they want to start all over
    another_game = None

    while another_game not in continue_choice:
        another_game = str(input(f'{continue_message}')).upper()

        if another_game == 'Y':
            sleep(1)
            clear()
            rps_game()
            break

        if another_game == 'N':
            clear()
            reveal_text("Thank you for playing and till next time!")
            sleep(3.5)
            clear()
            return

        elif another_game != 'Y':
            print(redt("Please enter 'Y' for Yes or 'N' for No.\n"))


if __name__ == "__main__":
    rps_game()
