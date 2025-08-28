# Use raw strings for file paths to avoid escape character issues
f1 = open(r"C:\Users\savin\OneDrive\Desktop\AI.28-08-25.txt", "w")
f2 = open(r"C:\Users\savin\OneDrive\Desktop\AI.f2.txt", "w")
f1.write("First file content\n")
f2.write("Second file content\n")
f1.close()
f2.close()

print("Files written successfully")