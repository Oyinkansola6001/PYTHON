import random

# this is scores for the game.
computer_score = 0    
my_score = 0

# different choices the game can have
game_choices = ["rock", "paper", "scissors"]     

print("Welcome to our mini game!")

while True:
    my_choice = input(str(game_choices) + " Put in your choice: ")
    computer_choice = random.choices(game_choices)
    
    computer_choice = computer_choice[0] 
    print("Computer choice: " + computer_choice)

    if my_choice == "rock" and computer_choice == "scissors":
        print("You win, computer lost.")
        my_score = my_score + 1
    elif my_choice == "paper" and computer_choice == "rock":
        print("You win, computer lost.")
        my_score = my_score + 1
    elif my_choice == "scissors" and computer_choice == "paper":
        print("You win, computer lost.")
        my_score = my_score + 1
    elif my_choice == "scissors" and computer_choice == "rock":
        print("Computer wins, you lost.")
        computer_score = computer_score + 1
    elif my_choice == "rock" and computer_choice == "paper":
        print("Computer wins, you lost.")
        computer_score = computer_score + 1
    elif my_choice == "paper" and computer_choice == "scissors":
        print("Computer wins, you lost.")
        computer_score = computer_score + 1
    else:
        print("It's a tie.")

    print("My score is: " + str(my_score) + " , computer score is: " + str(computer_score))

    



       

