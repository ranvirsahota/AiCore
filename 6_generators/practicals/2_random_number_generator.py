# Create a generator that yields random numbers.
import random
def rnd_generator():
    yield random.randint(3,7)

print(next(rnd_generator()))