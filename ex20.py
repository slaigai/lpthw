from sys import argv

script, input_file = argv


def print_all(f):
    # Print all lines from the file f
    print(f.read())


def rewind(f):
    # Reset cursor to beginning of file
    # The position passed into the seek function is in BYTES not lines. This function moves the cursor to the 0 byte
    f.seek(0)


def print_a_line(line_count, f):
    # Print the next line
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the while file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)

current_file.close()
