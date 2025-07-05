## User input as list item i.e Rock , Paper, Scissor same as it is.

import random

list_item = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice: \n")
# user_choice = user_choice.lower()
computer_choice = random.choice(list_item)
print(f"Computer choice: {computer_choice} \n")

if user_choice == computer_choice:
    print("Both choice: Match is Tie \n")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock: Computer Wins!")
    else:
        print("Rock smashed Scissor: User Wins!")

elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts the Paper: Computer Wins!")
    else:
        print("Paper covers the Rock: User Wins!")

elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock smashed Scissor: Computer Wins!")
    else:
        print("Scissor cuts the Paper: User Win!")
