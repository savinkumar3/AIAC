def collect_and_read_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    user_data['email'] = input("Enter your email: ")

    print("\nCollected User Data:")
    print(f"Name: {user_data['name']}")
    print(f"Age: {user_data['age']}")
    print(f"Email: {user_data['email']}")

# Example usage
if __name__ == "__main__":
    collect_and_read_user_data()