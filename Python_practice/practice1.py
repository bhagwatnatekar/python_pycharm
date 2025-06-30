# Write a code which will keep adding a stream of numbers inputted by user.
# The adding stops as soon as user presses quite "q" on key keyboard.

sum = 0
# While loop is used to repetitive task
while (True):
    #taking user input
    user_input = input("Enter the price: or press q to quite \n")
    #Conditon checks
    if user_input != "q":
        #operation to perform
        sum = sum + int(user_input)
        print(f"Your total bill is: {sum}")
    else:
        print("Code Ended!")



