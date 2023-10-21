# Create a generator that yields the square of every number up to 100, if that number is even or is a multiple of 3.
def sqaure_numbers():
    number = 1
    while number <= 100:
        if number % 2 == 0 or number % 3 == 0:
            yield number ** 2
        number += 1

# Turn the above generator into a generator comprehension.
ls_sqaure_numbers = (number ** 2 for number in range(1, 100) if number % 2 == 0 or number % 3 == 0)

for i in ls_sqaure_numbers:
    print(i)