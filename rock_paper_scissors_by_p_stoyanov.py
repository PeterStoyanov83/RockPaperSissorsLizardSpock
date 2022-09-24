import random


rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""
player_move = ""
computer_points = 0
player_points = 0

command = input("Choose [r]ock, [p]aper or [s]cissors : ")
while command != "No":
    command = player_move
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors


    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_points += 1
        print("YOU WIN!!!")

    elif player_move == computer_move:
        print("It's a Draw!")
    else:
        print("You lose!")
        computer_points += 1
    print(f"Player   = {player_points}")
    print(f"Computer = {computer_points}")
    command = input("Play Another Game ? [y]es or [n]o? : ")
    if command == "y":
        command = input("Choose [r]ock, [p]aper or [s]cissors : ")
    elif command == "n":
        break

print("Thank you for playing")
