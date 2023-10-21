# Using 2 yield statements, create a generator which alternatively yields yes and no.

def yes_or_no():
    while True:
        yield 'yes'
        yield 'no'

for i in yes_or_no():
    print(i)