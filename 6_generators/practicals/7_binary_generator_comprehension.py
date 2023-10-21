# Create an generator comprehension that infinitely generates ones or zeros randomly.
import random

infinite_binary = (random.choice(['0', '1']) for _ in iter(int, 1))

for binary in infinite_binary:
    print(binary, end = '')