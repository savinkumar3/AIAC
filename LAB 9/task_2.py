"""
Task 2: Student Management System
Simple student management with fee updates.
This program creates student objects and manages their fee payments.
"""


class sru_student:  # Student class for SRU university
    def __init__(self, name, roll_no, hostel_status, fee=0):  # Constructor to initialize student
        self.name = name  # Store student's name
        self.roll_no = roll_no  # Store student's roll number
        self.hostel_status = hostel_status  # Store whether student lives in hostel or not
        self.fee = fee  # Store the fee amount (starts at 0 if not provided)

    def fee_update(self, amount):  # Method to add more fee to existing fee
        self.fee += amount  # Add the new amount to current fee
        print(f"Fee updated successfully! Current fee: {self.fee}")  # Show confirmation message

    def display_details(self):  # Method to show all student information
        print("\n--- Student Details ---")  # Print a header
        print(f"Name          : {self.name}")  # Display student name
        print(f"Roll No       : {self.roll_no}")  # Display roll number
        print(f"Hostel Status : {self.hostel_status}")  # Display hostel status
        print(f"Total Fee     : {self.fee}")  # Display total fee amount


# Get student information from user
name = input("Enter student name: ")  # Ask for student's name
roll_no = int(input("Enter roll number: "))  # Ask for roll number and convert to integer
hostel_status = input("Enter hostel status (Hosteller/Day Scholar): ")  # Ask for hostel status
fee = int(input("Enter initial fee: "))  # Ask for initial fee and convert to integer

# Create student object with the information provided
student = sru_student(name, roll_no, hostel_status, fee)  # Make a new student object
student.display_details()  # Show the student's details

# Ask for additional fee and update
more_fee = int(input("\nEnter fee amount to update: "))  # Ask for additional fee amount
student.fee_update(more_fee)  # Add the additional fee to student's total
student.display_details()  # Show updated student details
