import random
list_item = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice: \n").lower()
computer_choice = random.choice(list_item)

print(f"User choice : {user_choice}, computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("Both choice: Match is Tie \n")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers rock: Computer Wins!")
    else:
        print("Rock smashed scissor: User Wins!")

elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts the paper: Computer Wins!")
    else:
        print("Paper covers the rock: User Wins!")

elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock samshed scissor: Computer Wins!")
    else:
        print("Scissor cuts the paper: User Win!")
        
