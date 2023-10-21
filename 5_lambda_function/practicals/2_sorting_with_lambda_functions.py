# Create a list with 5 tuples, where each tuple contains a name and a number. 
names = [
    ('five', 5),
    ('fifty-six', 56),
    ('ten', 10),
    ('six hundred sixty-six ', 666),
    ('fifteen', 15)
    ]
# Then, using the sort function, create a lambda function for each of the following bullet points:
# 1. Sort the list by the number in each tuple
print('1. Sort the list by the number in each tuple: ', sorted(names, key = lambda element: element[1]))

# 2. Sort the list by the name in each tuple
print('2. Sort the list by the name in each tuple: ', sorted(names, key = lambda element: element[0]))

# 3. Sort the list by the length of the name in each tuple
print('3. Sort the list by the length of the name in each tuple: ', sorted(names, key = lambda element: len(element[0])))

# 4. Sort the list by the length of the name in each tuple, but in reverse order
print('4. Sort the list by the length of the name in each tuple, but in reverse order:', sorted(names, reverse = True, key = lambda element: len(element[0])))