import art
print(art.logo)

# Define functions for mathematical operations.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Compile functions into a dictionary.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/" : divide,
}
# Define the main loop.
# Initialize a choice value for loop flow convenience later.
# Catch exceptions if the input is not a float value.
while True:
    choice = 0
    num1 = input("What's the first number?: ")
    try:
        num1 = float(num1)
    except ValueError:
        print("Please enter numbers only.")
        continue
    num1 = float(num1)
# Define the calculation loop.
# Catch invalid operator inputs.
# Catch exceptions for non-float numbers.
# Calculate and display results in 2-decimal format.
    while choice != "n":
        print("+\n-\n*\n/")
        operator = input("Pick an operation: ")
        if operator not in operations:
            print("Please only enter +, -, * or /.")
            continue
        while True:
            num2 = input("What's the next number?: ")
            try:
                num2 = float(num2)
            except ValueError:
                print("Please enter numbers only.")
                continue
            num2 = float(num2)
            break
        result = operations[operator](num1, num2)
        print(f"{num1:.2f} {operator} {num2:.2f} = {result:.2f}")
# Define choice loop (nested in calculation loop).
# If 'y', then assign the result to num1 and break to the calculation loop.
# Choice 'n' will break to the main loop because of the condition in the calculation loop.
# If 'n', then clear the screen and refresh the logo before looping.
# If 'q', exit the program.
# Catch invalid entries and ask again.
        while True:
            choice = input(f"Type 'y' to continue calculating with {result:.2f}, 'n' to start a new calculation, or 'q' to quit: ")
            if choice == "y":
                num1 = result
                break
            elif choice == "n":
                print("\n" * 50)
                print(art.logo)
                break
            elif choice == "q":
                print("Goodbye!")
                exit()
            else:
                print("Please enter 'y', 'n', or 'q' only.")
                continue
