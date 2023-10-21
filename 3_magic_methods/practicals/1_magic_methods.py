# 1. Create a class called 'Vecotr'
# 2. Define its initialiser so that it takes in a list of numbers as a an argument
# 3. Create an instance of the vector
# 4. Define the __repr__ magic method to define what is printed when we print the object. It's up to what his should look like
# 5. Define how you add two vector objects together. Again, your choice whether to add them element-wise or concatenate them
# 6. Define how you index an item in a vector

class Vector:

    def __init__(self, numbers):
        self.numbers = numbers
    
    def __repr__(self):
        return 'nothing'
    
    def __add__(self, other_numbers):
        sum = 0
        return map(lambda x, y: x + y, self.numbers, other_numbers)
    

    def __getitem__(self, idx):
        return self.numbers[idx]
    

vector_1 = Vector([1,2,3])
print(vector_1)
vector_2 = Vector([3,2,1])
print(vector_2)

vector_sum = list(vector_1 + vector_2)
print(vector_sum)

print(vector_1[1])
print(vector_2[2])
print(vector_sum[0])