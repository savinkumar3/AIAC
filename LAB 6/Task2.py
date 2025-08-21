def multiples(num):
    print(f"Multiples of {num} are:")
    for i in range(1, 11):
        print(num * i)

# Take input first
num = int(input("Enter the number to know the first 10 multiples: "))
multiples(num)
