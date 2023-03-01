import art
import sys

# A calculator w/out exit, great o_O

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    ans = 0
    try:
        ans = n1 / n2 
    except ZeroDivisionError:
        print("Division by zero")
        sys.exit(1)
    

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))
        calc_function = operations[operation]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

print(art.calc)
calculator()

