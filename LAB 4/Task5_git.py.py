file_path = r"C:\Users\savin\OneDrive\Desktop\AI.1.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")