import getpass

def collect_user_data():
    # Collect user data
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # Ask for password (input hidden)
    password = getpass.getpass("Set a password to protect your data: ")

    print("\nData collected successfully!\n")

    # Function to mask email (hide the part before @)
    def mask_email(email):
        at_index = email.find('@')
        if at_index != -1:
            return '*' * at_index + email[at_index:]
        return email

    # Show collected data with masked email
    print("User Data:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {mask_email(email)}")  # Hide important details

# Run the function
if __name__ == "__main__":
    collect_user_data()