def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise
    except OSError as e:
        raise e
if __name__ == "__main__":
    filename = r"C:\\Users\\savin\\OneDrive\\Desktop\\AI Ass\\LAB 13\\AI_LAb13.txt"
    try:
        content = read_file(filename)
        print(content)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"Error reading file: {e}")