import random

player_choice = input("Enter Rock, Paper or Scissors: ")
standardized_choice = player_choice.lower()

options = ['rock', "paper", "scissors"]

computer_choice = random.choice(options)

if computer_choice == player_choice:
    print("It is a TIE!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("YOU WIN ROCK BEATS SCISSORS!")
elif player_choice == "paper" and computer_choice == "rock":
    print("YOU WIN PAPER BEATS ROCK!")
elif player_choice == 'scissors' and computer_choice == "paper":
    print("YOU WIN SCISSORS BEATS PAPER!")
else:
    print("YOU LOSE!!!!")


