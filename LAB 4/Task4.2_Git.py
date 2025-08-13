# Program to count the number of vowels in a user input string

# Get input from user
input_str = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for char in input_str:
    if char in vowels:
        count += 1

# Display result
print(f"No.of.vowels={count}")