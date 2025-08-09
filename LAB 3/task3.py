# Step 1: Basic power bill calculation
def calculate_power_bill(units, rate_per_unit):
    return units * rate_per_unit

# Step 2: Add input from user
def main():
    try:
        units = float(input("Enter the number of units consumed: "))
        rate_per_unit = float(input("Enter the rate per unit: "))
        bill = calculate_power_bill(units, rate_per_unit)
        print(f"Your power bill is: {bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Step 3: Add slab-wise calculation for improved accuracy
def calculate_power_bill_slab(units):
    # Example slab rates:
    # First 100 units: 5 per unit
    # Next 100 units: 7 per unit
    # Above 200 units: 10 per unit
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill

# Step 4: Ask user if they want slab calculation
def improved_main():
    try:
        units = float(input("Enter the number of units consumed: "))
        use_slab = input("Use slab calculation? (y/n): ").strip().lower()
        if use_slab == 'y':
            bill = calculate_power_bill_slab(units)
        else:
            rate_per_unit = float(input("Enter the rate per unit: "))
            bill = calculate_power_bill(units, rate_per_unit)
        print(f"Your power bill is: {bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    print("Power Bill Calculator")
    improved_main()
