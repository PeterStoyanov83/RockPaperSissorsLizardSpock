import random

from termcolor import colored, cprint

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
lizard = "Lizard"
spock = "Spock"
computer_move = ""
player_move = ""
computer_points = 0
player_points = 0
computer_random_number = random.randint(1, 5)

command = input(colored("Choose [r]ock, [p]aper, [s]cissors [l]izard or Sp[o]ck : ", 'red'))
while command != "n":
    player_move = command
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    elif player_move == "l":
        player_move = lizard
    elif player_move == "o":
        player_move = spock

    else:
        raise SystemExit("Invalid Move try again...")

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    elif computer_random_number == 4:
        computer_move = lizard
    else:
        computer_move = spock

    cprint(f"The computer chose {computer_move}.", "green", )

    if player_move == computer_move:
        cprint("It's a Draw!", 'green', )
    elif player_move == rock and computer_move == scissors:
        player_points += 1
        cprint("Rock crushes scissors! YOU WIN!!!", 'yellow', )
    elif player_move == rock and computer_move == lizard:
        player_points += 1
        cprint("Rock crushes lizard! YOU WIN!!!", 'yellow', )
    elif player_move == paper and computer_move == rock:
        player_points += 1
        cprint("Paper covers rock! YOU WIN!!!", 'yellow', )
    elif player_move == scissors and computer_move == paper:
        player_points += 1
        cprint("Scissors cut paper! YOU WIN!!!", 'yellow', )
    elif player_move == scissors and computer_move == lizard:
        player_points += 1
        cprint("Scissors decapitate lizard ! YOU WIN!!!", 'yellow', )
    elif player_move == lizard and computer_move == paper:
        player_points += 1
        cprint("Lizard eats paper! YOU WIN!!!", 'yellow', )
    elif player_move == paper and computer_move == spock:
        player_points += 1
        cprint("Paper disproves Spock! YOU WIN!!!", 'yellow', )
    elif player_move == spock and computer_move == rock:
        player_points += 1
        cprint("Spock vaporises rock! YOU WIN!!!", 'yellow', )
    elif player_move == lizard and computer_move == spock:
        player_points += 1
        cprint("Lizard poisons Spock! YOU WIN!!!", 'yellow')
    elif player_move == spock and computer_move == scissors:
        player_points += 1
        cprint("Spock smashes scissors! YOU WIN!!!", 'yellow')

    elif computer_move == rock and player_move == scissors:
        computer_points += 1
        cprint("Rock crushes scissors! YOU LOSE!!!", 'red', )
    elif computer_move == rock and player_move == lizard:
        computer_points += 1
        cprint("Rock crushes lizard! YOU LOSE!!!", 'red', )
    elif computer_move == paper and player_move == rock:
        computer_points += 1
        cprint("Paper covers rock! YOU LOSE!!!", 'red', )
    elif computer_move == scissors and player_move == paper:
        computer_points += 1
        cprint("Scissors cut paper! YOU LOSE!!!", 'red', )
    elif computer_move == scissors and player_move == lizard:
        computer_points += 1
        cprint("Scissors decapitate lizard ! YOU LOSE!!!", 'red', )
    elif computer_move == lizard and player_move == paper:
        computer_points += 1
        cprint("Lizard eats paper! YOU LOSE!!!", 'red', )
    elif computer_move == paper and player_move == spock:
        computer_points += 1
        cprint("Paper disproves Spock! YOU LOSE!!!", 'red', )
    elif computer_move == spock and player_move == rock:
        computer_points += 1
        cprint("Spock vaporises rock! YOU LOSE!!!", 'red', )
    elif computer_move == lizard and player_move == spock:
        computer_points += 1
        cprint("Lizard poisons Spock! YOU LOSE!!!", 'red', )
    elif computer_move == spock and player_move == scissors:
        computer_points += 1
        cprint("Spock smashes scissors! YOU LOSE!!!", 'red',)

    cprint(f"Player   = {player_points}", 'yellow', )
    cprint(f"Computer = {computer_points}", 'yellow', )

    command = input(colored("Play Another Game ? [y]es or [n]o? : ", 'cyan', ))
    if command == "y":
        command = input(colored("Choose [r]ock, [p]aper, [s]cissors [l]izard or Sp[o]ck : ", 'red', ))
    elif command != "n":
        break
print()
cprint("Thank you for playing", 'red', )
