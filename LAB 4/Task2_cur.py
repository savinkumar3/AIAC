def cm_to_inches(cm):
    """
    Converts centimeters to inches.
    1 centimeter = 0.39 inch
    """
    return cm * 0.39

# Example usage:
centimeters = float(input("Enter length in centimeters: "))
inches = cm_to_inches(centimeters)
print(f"{centimeters} centimeters is equal to {inches} inches.")
