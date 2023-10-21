# Create a generator that takes in an integer as an input and returns random passwords with a length equal to the passed integer.
# To make the password more robust, the characters should include uppercase letters, numbers and special characters.

import secrets
import string

def generate_random_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        yield password

for i in range(10):
    print(next(generate_random_password(12)))
