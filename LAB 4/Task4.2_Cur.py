def count_vowels_in_string():
    user_input = input()
    vowels = "aeiouAEIOU"
    count = 0
    for char in user_input:
        if char in vowels:
            count += 1
    print(f"No.of.vowels={count}")

# Example usage:
# Input: Namaste
# Output: No.of.vowels=3
count_vowels_in_string()

