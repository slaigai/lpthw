from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# indata = open(from_file).read()
# This also does a close so you don't have to close the file at the end
in_file = open(from_file)
indata = in_file.read()

# Note expression evaluation in {}
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Read, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# Note use the following command from terminal to quickly create a text file
# echo "This is a test file." > test.txt

# Show file contents using cat
# cat test.txt

# Use man echo or man cat to learn more about these commands


