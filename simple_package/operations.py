###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

import math

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

def power(a, b):
    """Raises the first number to the power of the second."""
    return a ** b

def square_root(a):
    """Calculates the square root of a number."""
    # math.sqrt will raise a ValueError for negative numbers
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)

def logarithm(a, base=math.e):
    """Calculates the natural log (base e) or log with a specified base."""
    if a <= 0:
        raise ValueError("Logarithm input must be greater than zero.")
    return math.log(a, base)

def calculator():

    try:
        import math
    except ImportError:
        print("Error: math module is not available.")
        return
    
    operations = {
        'add': (add, 2),
        'sub': (subtract, 2),
        'mul': (multiply, 2),
        'div': (divide, 2),
        'pow': (power, 2),
        'sqrt': (square_root, 1),
        'log': (logarithm, 1)
    }

    print("Welcome to the calculator! Type 'exit' to quit.")
    print("Commands: add, sub, mul, div, pow, sqrt, log")

    while True:
        user_input = input("Enter operation and numbers: ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        parts = user_input.split()
        if len(parts) < 2:
            print("Error: Not enough input. Please provide an operation and numbers.")
            continue

        operation = parts[0]
        if operation not in operations:
            print(f"Error: Unknown operation '{operation}'.")
            continue

        func, num_args = operations[operation]
        if len(parts) - 1 != num_args:
            print(f"Error: '{operation}' requires {num_args} arguments.")
            continue

        try:
            args = [float(part) for part in parts[1:num_args + 1]]
            result = func(*args)
            print(f"The result of {operation} is: {result:.3f}")
        except ValueError as ve:
            print(f"Value Error: {ve}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

