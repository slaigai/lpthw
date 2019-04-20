# Finally, reading files...

# Don't want to hard code the file name

from sys import argv

# Unpack the command line args
script, filename = argv

# I'm assuming the "with" context manager will be introduced later?
# Returns a file object. If file cannot be opened, an OSError is raised.
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())  # use the read function of the file object to read the text in the open file

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())

# Close the files (this should have been in the example code IMO).
txt.close()
txt_again.close()

# Note python does not restrict from opening a file twice. Sometimes, this is necessary

