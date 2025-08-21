class Student:
    def __init__(self):
        self.roll = 0
        self.marks = 0
        self.name = ""

    def input_details(self):
        self.name = input("Enter your Name: ")
        self.roll = int(input("Enter your Roll No: "))
        self.marks = int(input("Enter your Marks: "))

    def display_grade(self):
        if self.marks >= 90:
            print("You got A grade")
        elif self.marks <90 and self.marks>=75 :
            print("You got B grade")
        elif self.marks <75 and self.marks>=60:
            print("You got C grade")
        else:
            print("Better Luck Next time")


# Main function
def main():
    s = Student()
    s.input_details()
    s.display_grade()


if __name__ == "__main__":
    main()
