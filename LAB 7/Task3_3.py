
with open("input.txt", "r") as input_file:
    data = input_file.readlines()

with open("output.txt", "w") as output_file:
    for line in data:
        output_file.write(line.upper())

print("Processing done")
