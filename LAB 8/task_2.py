def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input: Score must be a number."
    if score < 0 or score > 100:
        return "Invalid input: Score must be between 0 and 100."
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    user_input = input("Enter the score (0-100): ")
    score = float(user_input)
    print("Grade:", assign_grade(score))
except ValueError:
    print("Invalid input: Please enter a numeric value.")