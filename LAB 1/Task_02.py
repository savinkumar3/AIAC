def max_of_three(numbers):
    if len(numbers) != 3:
        raise ValueError("Input list must contain exactly three numbers.")
    return max(numbers)

# Example usage:
nums = [int(input("Enter number {}: ".format(i+1))) for i in range(3)]
print("The maximum number is:", max_of_three(nums))