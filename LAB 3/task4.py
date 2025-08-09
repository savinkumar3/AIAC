users_db = {}

def register_user():
    print("=== Register User ===")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please try a different one.")
        return
    password = input("Enter a password: ")
    users_db[username] = password
    print("Registration successful!")

def login_user():
    print("=== Login User ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Login failed. Invalid username or password.")

# Example usage:
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
