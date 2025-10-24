# 1- Write to File
print("<==== Write to File ===>")
with open("example.txt", "w") as f:  # 'w' = write (overwrites)
    f.write("Hello, world!\n")
    f.write("Python file handling example.\n")
print("File written successfully.")


# 2- Read Entire File
print("\n<==== Read Entire File ===>")
with open("example.txt", "r") as f:  # 'r' = read
    content = f.read()
    print(content)
    
    """
        when use f.read(), it reads the entire file at once.
        pointer moves to the end of the file after reading.
        so you have to use : f.seek(0) to reset pointer to the beginning
    """
    # you can loop through lines using:
    print("<==== Reading line by line ===>")
    f.seek(0)  # Reset pointer to the beginning
    for line in f:
        print(line.strip())

# 3- Append to File
print("\n<==== Append to File ===>")
with open("example.txt", "a") as f:  # 'a' = append
    f.write("Adding a new line.\n")
print("Line appended.")


# 4- File Info
print("\n<==== File Info ===>")
with open("example.txt", "r") as f:
    print("File Name:", f.name)
    print("Mode:", f.mode)
print("Closed:", f.closed)


# 5- Exception Handling
print("\n<==== Exception Handling ===>")
try:
    with open("not_found.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")
