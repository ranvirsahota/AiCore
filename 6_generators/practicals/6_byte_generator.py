# Create a loop which iterates through a generator you define that generates incrementing binary bytes (8 digit numbers containing only ones and zeros) up to 256.
#   128  64  32  16  8  4  2 1
def binary_bytes_generator():
    for i in range(256):
        yield format(i, '000000008b')

# Example usage: Iterate through the generator
for binary_byte in binary_bytes_generator():
    print(binary_byte)
