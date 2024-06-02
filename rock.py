import random


choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Select the following:\n'rock, paper, scissors': ")

    if user_choice not in choices:
        break

    computer_choice = random.choice(choices)
    print("user choice is: ", user_choice)
    print("computer choice is: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie")
        user_score += 1
        computer_score += 1

    elif user_choice == "rock" and computer_choice == "scissors":
        print("User Wins")
        user_score += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("User Wins")
        user_score += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("User Wins")
        user_score += 1

    else:
        print("Computer Wins")
        computer_score += 1

    print("User score is: ", user_score)
    print("Computer score is: ", computer_score)

    prompt = input("If you wanna play another round (y/n): ")

    if prompt == "y":
        continue
    elif prompt == "n":
        break
    else:
        print("Invalid input")