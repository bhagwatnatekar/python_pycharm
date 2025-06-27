import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Defining List
game_item = [rock, paper, scissor]

#User choice
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissor"))
if user_choice >= 2 or user_choice < 0:
    print(f"user_choice: ")
    print(game_item[user_choice])

#Computer choice
computer_choice = random.randint(0,2)
print(f"computer_choice: ")
print(game_item[computer_choice]) #print list with index input

#Conditions
if user_choice >= 3 or user_choice < 0:
    print("Invalid entry, Game end")
elif user_choice == computer_choice:
    print("Match Tie!")
elif user_choice == 0 and computer_choice == 2:
    print("User Wins!")
elif computer_choice == 0 and user_choice == 2:
    print("Computer Wins!")
elif user_choice > computer_choice:
    print("User Wins!")
elif computer_choice > user_choice:
    print("Computer Wins!")
# else:
#     print("invalid input, Game End")
