import random

from termcolor import colored, cprint

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""
player_move = ""
computer_points = 0
player_points = 0
computer_random_number = random.randint(1, 3)

command = input(colored("Choose [r]ock, [p]aper or [s]cissors : ", 'red'))
while command != "n":
    player_move = command
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Move try again...")

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    cprint(f"The computer chose {computer_move}.", "green", )
    if player_move == computer_move:
        cprint("It's a Draw!", 'green', )
    elif (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_points += 1
        cprint("YOU WIN!!!", 'yellow', )
    else:
        cprint("You lose!", 'red', )
        computer_points += 1
    cprint(f"Player   = {player_points}", 'yellow', )
    cprint(f"Computer = {computer_points}", 'yellow', )
    command = input(colored("Play Another Game ? [y]es or [n]o? : ", 'cyan', ))
    if command == "y":
        command = input(colored("Choose [r]ock, [p]aper or [s]cissors : ", 'red', ))
    elif command != "n":
        break
print()
cprint("Thank you for playing", 'red', )
