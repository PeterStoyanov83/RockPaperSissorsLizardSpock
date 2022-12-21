import random

from termcolor import colored, cprint

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"
LIZARD = "Lizard"
SPOCK = "Spock"
COMPUTER_MOVE = ""
PLAYER_MOVE = ""
COMPUTER_POINTS = 0
PLAYER_POINTS = 0
COMPUTER_RANDOM_NUMBER = random.randint(1, 5)

command = input(colored("Choose [r]ock, [p]aper, [s]cissors [l]izard or Sp[o]ck : ", 'red'))
while command not in "r" and command not in "p" and command not in "s" and command not in "l" and command not in "o":
    cprint("Choose the right command", 'blue',)
while command != "n":
    PLAYER_MOVE = command
    if PLAYER_MOVE == "r":
        PLAYER_MOVE = ROCK
    elif PLAYER_MOVE == "p":
        PLAYER_MOVE = PAPER
    elif PLAYER_MOVE == "s":
        PLAYER_MOVE = SCISSORS
    elif PLAYER_MOVE == "l":
        PLAYER_MOVE = LIZARD
    elif PLAYER_MOVE == "o":
        PLAYER_MOVE = SPOCK

    else:
        raise SystemExit("Invalid Move try again...")

    if COMPUTER_RANDOM_NUMBER == 1:
        COMPUTER_MOVE = ROCK
    elif COMPUTER_RANDOM_NUMBER == 2:
        COMPUTER_MOVE = PAPER
    elif COMPUTER_RANDOM_NUMBER == 3:
        COMPUTER_MOVE = SCISSORS
    elif COMPUTER_RANDOM_NUMBER == 4:
        COMPUTER_MOVE = LIZARD
    else:
        COMPUTER_MOVE = SPOCK

    cprint(f"The computer chose {COMPUTER_MOVE}.", "green", )

    if PLAYER_MOVE == COMPUTER_MOVE:
        cprint("It's a Draw!", 'green', )
    elif PLAYER_MOVE == ROCK and COMPUTER_MOVE == SCISSORS:
        PLAYER_POINTS += 1
        cprint("Rock crushes scissors! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == ROCK and COMPUTER_MOVE == LIZARD:
        PLAYER_POINTS += 1
        cprint("Rock crushes lizard! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == PAPER and COMPUTER_MOVE == ROCK:
        PLAYER_POINTS += 1
        cprint("Paper covers rock! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == SCISSORS and COMPUTER_MOVE == PAPER:
        PLAYER_POINTS += 1
        cprint("Scissors cut paper! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == SCISSORS and COMPUTER_MOVE == LIZARD:
        PLAYER_POINTS += 1
        cprint("Scissors decapitate lizard ! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == LIZARD and COMPUTER_MOVE == PAPER:
        PLAYER_POINTS += 1
        cprint("Lizard eats paper! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == PAPER and COMPUTER_MOVE == SPOCK:
        PLAYER_POINTS += 1
        cprint("Paper disproves Spock! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == SPOCK and COMPUTER_MOVE == ROCK:
        PLAYER_POINTS += 1
        cprint("Spock vaporises rock! YOU WIN!!!", 'yellow', )
    elif PLAYER_MOVE == LIZARD and COMPUTER_MOVE == SPOCK:
        PLAYER_POINTS += 1
        cprint("Lizard poisons Spock! YOU WIN!!!", 'yellow')
    elif PLAYER_MOVE == SPOCK and COMPUTER_MOVE == SCISSORS:
        PLAYER_POINTS += 1
        cprint("Spock smashes scissors! YOU WIN!!!", 'yellow')

    elif COMPUTER_MOVE == ROCK and PLAYER_MOVE == SCISSORS:
        COMPUTER_POINTS += 1
        cprint("Rock crushes scissors! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == ROCK and PLAYER_MOVE == LIZARD:
        COMPUTER_POINTS += 1
        cprint("Rock crushes lizard! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == PAPER and PLAYER_MOVE == ROCK:
        COMPUTER_POINTS += 1
        cprint("Paper covers rock! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == SCISSORS and PLAYER_MOVE == PAPER:
        COMPUTER_POINTS += 1
        cprint("Scissors cut paper! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == SCISSORS and PLAYER_MOVE == LIZARD:
        COMPUTER_POINTS += 1
        cprint("Scissors decapitate lizard ! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == LIZARD and PLAYER_MOVE == PAPER:
        COMPUTER_POINTS += 1
        cprint("Lizard eats paper! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == PAPER and PLAYER_MOVE == SPOCK:
        COMPUTER_POINTS += 1
        cprint("Paper disproves Spock! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == SPOCK and PLAYER_MOVE == ROCK:
        COMPUTER_POINTS += 1
        cprint("Spock vaporises rock! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == LIZARD and PLAYER_MOVE == SPOCK:
        COMPUTER_POINTS += 1
        cprint("Lizard poisons Spock! YOU LOSE!!!", 'red', )
    elif COMPUTER_MOVE == SPOCK and PLAYER_MOVE == SCISSORS:
        COMPUTER_POINTS += 1
        cprint("Spock smashes scissors! YOU LOSE!!!", 'red',)

    cprint(f"Player   = {PLAYER_POINTS}", 'yellow', )
    cprint(f"Computer = {COMPUTER_POINTS}", 'yellow', )

    command = input(colored("Play Another Game ? [y]es or [n]o? : ", 'cyan', ))
    if command == "y":
        command = input(colored("Choose [r]ock, [p]aper, [s]cissors [l]izard or Sp[o]ck : ", 'red', ))
    elif command != "n":
        break
print()
cprint("Thank you for playing", 'red', )
