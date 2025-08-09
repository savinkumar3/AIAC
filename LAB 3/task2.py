def main():
    # Take input from the user as a string of numbers separated by spaces
    input_str = input("Enter numbers separated by spaces: ")
    # Split the string into a list and convert each element to an integer
    num_list = [int(x) for x in input_str.split()]
    # Sort the list using the built-in sorted() function
    sorted_list = sorted(num_list)
    # Output the sorted list
    print("Sorted numbers:", sorted_list)

if __name__ == "__main__":
    main()


