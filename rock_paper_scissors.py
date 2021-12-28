import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? Choose wisely: ").lower()

    if player == computer:
        print("computer has chosen:", computer)
        print("You have chosen:", player)
        print("Draw! Please play again")
    elif player == "rock":
        if computer == "paper":
            print("computer has chosen:", computer)
            print("You have chosen:", player)
            print("Sorry! You lose")
        elif computer == "scissors":
            print("computer has chosen:", computer)
            print("You have chosen:", player)
            print("Congratulations! You win")
    elif player == "scissors":
        if computer == "rock":
            print("computer has chosen:", computer)
            print("You have chosen:", player)
            print("Sorry! You lose")
        elif computer == "paper":
            print("computer has chosen:", computer)
            print("You have chosen:", player)
            print("Congratulations! You win")
    elif player == "paper":
        if computer == "scissors":
            print("computer has chosen:", computer)
            print("You have chosen:", player)
            print("Sorry! You lose")
        elif computer == "rock":
            print("computer has chosen:", computer)
            print("You have chosen:", player)
            print("Congratulations! You win")

    play_again = None
    yes_or_no = ["y", "n"]
    while play_again not in yes_or_no:
        play_again = input("Would you like to play again? (y/n): ").lower()

    if play_again.lower() != "y":
        print("Thanks for playing!")
        break