def cm_to_inches():
    try:
        cm = float(input("Enter length in centimeters: "))
        inches = cm * 0.39
        print(f"{cm} cm is equal to {inches:.2f} inches.")
    except ValueError:
        print("Please enter a valid number.")

# Example usage
if __name__ == "__main__":
    cm_to_inches()