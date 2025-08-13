def format_full_name(full_name):
    """
    Reads a full name and formats it as 'Last, First'.
    Assumes the full name consists of two words: first name and last name.
    """
    parts = full_name.strip().split()
    if len(parts) != 2:
        raise ValueError("Full name must contain exactly two words: first and last name.")
    first_name, last_name = parts
    return f"{last_name}, {first_name}"

# Example usage:
if __name__ == "__main__":
    names = [input () ]
    for name in names:
        formatted = format_full_name(name)
        print(formatted)