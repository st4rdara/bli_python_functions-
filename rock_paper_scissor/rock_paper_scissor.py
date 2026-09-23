import random

print("Rock Paper Scissors!")
print("Choose rock, paper, or scissors.")

choices = ["rock", "paper", "scissors"]

player = input("Enter your choice: ")
computer = random.choice(choices)

print("Computer chose:", computer)

if player == computer:
    print("It's a draw!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

elif player in choices:
    print("Computer wins!")

else:
    print("Invalid choice!")
