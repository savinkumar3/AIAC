def format_full_name():
    full_name = input("Enter full name : ").strip()
    # Split the name into parts
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Please enter both first and last names.")
        return
    first_name = name_parts[0]
    last_name = name_parts[-1]
    print(f"First name : {first_name}")
    print(f"Last name : {last_name}")
    print(f"Formatted name: {last_name}, {first_name}")

# Example usage:
format_full_name()
