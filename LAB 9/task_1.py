"""
Task 1: Sum of Even and Odd Numbers

This program calculates the sum of even and odd numbers from a user-provided list.
The user enters a space-separated list of integers, and the program computes:
- Sum of all even numbers in the list
- Sum of all odd numbers in the list

Author: [Your Name]
Date: [Current Date]
"""


def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a given list.
    
    Args:
        numbers (list[int]): List of integers to process
    
    Returns:
        tuple: A tuple containing (sum_of_even_numbers, sum_of_odd_numbers)
    
    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)  # Even: 2+4=6, Odd: 1+3+5=9
    """
    sume = 0  # Initialize sum of even numbers to zero
    sumO = 0  # Initialize sum of odd numbers to zero
    
    for n in numbers:  # Iterate through each number in the list
        if n % 2 == 0:  # Check if the number is even
            sume += n  # Add even number to even sum
        else:  # If number is odd
            sumO += n  # Add odd number to odd sum
    
    return sume, sumO  # Return both sums as a tuple


# Get user input for numbers
raw = input("Enter numbers separated by spaces: ")  # Prompt user for input
numbers = [int(x) for x in raw.split()] if raw.strip() else []  # Convert string to list of integers

# Calculate sums using the function
sume, sumO = sum_even_odd(numbers)  # Call function to get even and odd sums

# Display results
print("Sum of Even Numbers:", sume)  # Print sum of even numbers
print("Sum of Odd Numbers:", sumO)  # Print sum of odd numbers
