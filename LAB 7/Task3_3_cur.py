with open("input.txt", "r") as input_file:
    data = input_file.readlines()

with open("output.txt", "w") as output:
    for line in data:
        output.write(line.upper())

print("Processing done")
    