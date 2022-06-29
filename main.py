import random

print(" Rock, Paper, Scissors By Tofu ")
print("------------------------------")

#user choice

userChoice = input("Enter (rock, paper, scissors): ")

#computer choice

choice = ["rock", "paper", "scissors"]
computerChoice = random.choice(choice)

print(f"\nComputer chose {computerChoice}. \nYou chose {userChoice}.")

#game result

if computerChoice == userChoice:
    print("Tie!")
elif computerChoice == "rock":
    if userChoice == "paper":
        print("You win!")
    else:
        print("You lose!")
elif computerChoice == "paper":
    if userChoice == "rock":
        print("You lose!")
    else:
        print("You win!")
elif computerChoice == "scissors":
    if userChoice == "rock":
        print("You lose!")
    else:
        print("You win!")

print("------------------------------")

