# Create a generator that takes in two numbers and yields all multiples of 3 between the two of them.
def multiples_of_3_generator(start, end):
    current = start if start % 3 == 0 else (start + (3 - start % 3))
    
    while current <= end:
        yield current
        current += 3

# Example usage
start = 10
end = 30
generator = multiples_of_3_generator(start, end)

for multiple in generator:
    print(multiple)
