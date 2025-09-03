def convert_date_format(date_str):
    parts = date_str.split('-')
    if len(parts) == 3:
        return f"{parts[2]}-{parts[1]}-{parts[0]}"
    else:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")

if __name__ == "__main__":
    date_input = input("Enter date in YYYY-MM-DD format: ")
    try:
        converted = convert_date_format(date_input)
        print("Converted date:", converted)
    except ValueError as e:
        print(e)




