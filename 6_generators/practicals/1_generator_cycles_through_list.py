# Create a generator that infinitely cycles through a list of items in order

def cyclic_gen(items):
    index = 0
    while True:
        yield items[index]
        index += 1
        if (len(items) == index): index = 0

numbers = [1, 2, 3, 4, 5, 6]
for i in cyclic_gen(numbers):
    print(i)