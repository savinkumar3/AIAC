"""
Task 3: Simple Calculator
A basic calculator program that performs arithmetic operations.
This program takes two numbers from user and performs addition, subtraction,
multiplication, and division operations.
"""


def add(a, b):  # Function to add two numbers
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b  # Return the sum of a and b


def subtract(a, b):  # Function to subtract two numbers
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number (minuend)
        b (float): Second number (subtrahend)
    
    Returns:
        float: Difference of a and b
    """
    return a - b  # Return the difference of a and b


def multiply(a, b):  # Function to multiply two numbers
    """
    Multiply two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b  # Return the product of a and b


def divide(a, b):  # Function to divide two numbers
    """
    Divide first number by second number.
    
    Args:
        a (float): Dividend (number to be divided)
        b (float): Divisor (number to divide by)
    
    Returns:
        float or str: Quotient of a and b, or error message if division by zero
    """
    if b != 0:  # Check if divisor is not zero
        return a / b  # Return the quotient if division is possible
    else:  # If divisor is zero
        return "Error! Division by zero."  # Return error message


# Main program execution
print("Simple Calculator")  # Display calculator title

# Get two numbers from user
num1 = float(input("Enter first number: "))  # Get first number and convert to float
num2 = float(input("Enter second number: "))  # Get second number and convert to float

print("\nResults:")  # Display results header

# Perform all operations and display results
print("Addition:", add(num1, num2))  # Add numbers and display result
print("Subtraction:", subtract(num1, num2))  # Subtract numbers and display result
print("Multiplication:", multiply(num1, num2))  # Multiply numbers and display result
print("Division:", divide(num1, num2))  # Divide numbers and display result
