# Calculator code
# Function define
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2
# Dictionary use for operands
operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
# Defining calculator function to easy use function again
def calcultor():
    should_accumulate = True # Continue the functionality
    n1 = float(input("What is the first number?: "))
    while should_accumulate: # used to check condition
        # Operation chooses to do
        for operator in operation:
            print(operator)
        operator = input(f"Pick an operation: ")
        # Enter second input number
        n2 = float(input("What is the second number?: "))
        # Calculating result and printing 3 + 2 : 5 likewise
        result = operation[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result} ")
        # Continue the code functionality with last result
        should_continue = input(f"Type 'y' to continue with {result}, or Type 'n' to start a new calculation: ")
        if should_continue == 'y':
            n1 = result
        else:
            should_accumulate = False # Distributing the calculation flow and start fresh calculation
            print("\n" * 10)
            calcultor() # Function call to start fresh

calcultor() # Function call