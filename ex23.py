import sys

# Try these encodings as well: utf-16, utf-32, big5
# big5 strict breaks stuff because it cant encode the first character
# big5 replace replaces stuff it cant encode/decode with a ? character
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    # If readline reaches the end of the file, an empty string is returned (an empty string is False)
    if line:
        # Base case EOF
        print_line(line, encoding, errors)
        # Recursion to get all lines without a loop (return value is not used)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # Strip away leading or trailing whitespace, particularly the trailing newline
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

languages.close()

# These examples use the utf-8, utf-16, and big5 encodings to demonstrate conversion and the types of errors you can
# get. Each of these names are called a codec. Python 3 uses the "encoding" parameter to pass in a codec.

# \x## where ## is interpreted in hex

# A byte is a sequence of 8 bits.
# 8 bits can only hold 256 numbers (0-255)

# ASCII -> American Standard Code for Information Interchange

# Try these in IDLE to print out the letter Z, number 90
# 0b1011010  # binary
# ord('Z')  # get number based on letter 'Z'
# chr(90)  # convert number to letter 'Z'

# Print out 'Zed A. Shaw
# for c in [90, 101, 100, 32, 65, 46, 32, 83, 104, 97, 119]:
#     print(chr(c), end='')

# Unicode is intended as the "universal encoding" of all human languages. Basically a MEGA ASCII table
# 32 bits to encode (2^32 = 4,294,967,295)
# Lots of wasted space if we always used 4 bytes to encode everything.
# Use escape chars so that most are encoded in 1 byte and escaped if more bytes are needed.
# The convention for encoding text in Python is called utf-8 "Unicode Transformation Format 8 Bits" for encoding
# Unicode characters into a sequence of bits. utf-8 is the current standard

# b'' is a byte string representation of the character data.
# b'\xe6\x96\x87\xe8\xa8\x80' <===> 文言
# Left is hexadecimal byte string representation of the utf-8 character outputs on the right
# Left is "raw bytes" and right is "cooked" to see the real characters
# Left is the encoded string, right is the decoded string

# In python, a string is a UTF-8 encoded sequence of characters for displaying or working with text. The bytes are
# the raw sequence of bytes that python uses to store this UTF-8 string and start with a b' to tell python you're
# working with raw bytes.
# Raw bytes have no convention to them (they're just a bunch of bits) and needed to be decoded into real text

# raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
# utf_string = "文言"
# raw_bytes.decode()
# utf_string.encode()
# raw_bytes == utf_string.encode()
# utf_string == raw_bytes.decode()

# DBES: Decode bytes, encode strings