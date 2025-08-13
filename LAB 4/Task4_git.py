# Count the number of vowels in a user-provided string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))