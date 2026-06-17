from platform import python_revision

import art



def add(n1, n2):
    return n1 + n2

#TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}

#TODO: use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

def calculator():
    print(art.logo)
    num1 = float(input("Whats the first number?: "))
    continue_calculating = True
    while continue_calculating:
        operation_symbol = input("+\n-\n*\n/\nPick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = (operations[operation_symbol](num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {result}")
        should_continue = input(
            f'''Type "y" to continue calculating with {result}, or type "n" to start a new calculation:''')
        if should_continue == "n":
            continue_calculating = False
            print("\n" * 20)
            calculator()

        elif should_continue == "y":
            num1=result


calculator()