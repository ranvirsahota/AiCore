# Create a list of 5 numbers
numbers = [1, 26, 122, 47, 23]

# Create the following lambda functions:
# 1. A lambda function that squares a number. Then use map to square each number in the list
sq = lambda x: x ** 2
squared_numbers = map(sq, numbers)
print('1. A lambda function that squares a number. Then use map to square each number in the list: ', list(squared_numbers))

# 2. A lambda function that cubes a number. Then use map to cube each number in the list
cube = lambda x: x ** 3
cube_numbers = map(cube, numbers)
print('2. A lambda function that cubes a number. Then use map to cube each number in the list: ', list(cube_numbers))

# 3. A lambda function that takes in a number and returns that number squared if it is even, and cubed if it is odd.
sq_or_cube = lambda x: sq(x) if x % 2 == 0 else cube(x)
# Then use map to apply the function to each number in the list.
sq_or_cube_numbers = map(sq_or_cube, numbers)
print('3. A lambda function that takes in a number and returns that number squared if it is even, and cubed if it is odd.\n' +
      '   Then use map to apply the function to each number in the list: ', list(sq_or_cube_numbers))