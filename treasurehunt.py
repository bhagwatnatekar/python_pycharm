#ASCII art input
print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
      ''')
#Welcome lines
print("Welcome to Treasure Hunt Game.")
print("Your mission is to find the treasure.")
#condition 1 direction to choose
direction = input('You\'re at a cross road. Where do you wnat to go? Type "left" or "right"\n') .lower()
if direction == "left":
#conditon 2 action to take
    action = input('You\'ve come to a lake. There is an island in the middle of the lake.'
                    ' Type "wait" to wait a boat. Type "swim" to swim across\n').lower()
    if action == "wait":
#condition 3 door to choose
        door = input('You arrive at the island unharmed. There is a house with 3 doors. '
                        'One red, one yellow and one blue. Which colour do you choose?\n').lower()
#nested if condition
        if door == "yellow":
            print("You win!")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Wrong input. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

