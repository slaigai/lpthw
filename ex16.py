"""
Remember these file object methods
close -- closes the file
read -- reads the contents of a file. you can assign the result to a variable
readline -- reads just one line of the text file
truncate -- empties the file. watch out if you care about the file
write('stuff') -- writes "stuff" to the file
seek(0) -- move the read/write location to the beginning of the file
"""

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

print("Opening the file...")
# Open the file in write mode. If file does not exist, one is created (I tried it out). Calling open with 'w' write
# mode will first truncate the file, so the truncate operation is actually not necessary.
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# Delete contents of the file (if new file, nothing happens)
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

# Note 'w' for write, 'r' for read (default), 'a' for writing and appending to file

# Note using the + modifier ('w+', 'r+', 'a+') will open the file in read and write mode. You can read and write
# depending on the position in the file.
