def count_lines_in_file():
    file_path = r"C:\Users\savin\OneDrive\Desktop\AI.1.txt"
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in the file: {len(lines)}")
    except FileNotFoundError:
        print("The file was not found.")

# Example usage:
count_lines_in_file()

