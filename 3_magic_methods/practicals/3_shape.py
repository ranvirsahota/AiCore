# 1. Define a class called Shape

# 2. Define its initialiser and initialise two attributes:
#   num_sides, which is required
#   tesselates, which is optional
#   raise an error if num_sides is zero

# 3. Define a method called get_info which returns a string telling us the number of sides of the shape and whether it tesselates or not.
#       For now, make this function raise a NotImplementedError if called.
#       That's because this is an "abstract base class", which means it should only be used when inherited from by other classes.
#       I.e. there should be no instances of this generic Shape class

# 4. Create the following classes which inherit from Shape
#       Circle
#       Triangle
#       Square
#       Pentagon
#       Hexagon

from abc import abstractclassmethod

class Shape:
    def __init__(self, num_sides, **kwargs):
        if num_sides == 0:
            assert ValueError


    @abstractclassmethod
    def get_info(self):
        assert NotImplementedError

class Circle(Shape):
    def get_info(self):
        return f'Side: {super.num_sides}\n Tesselate?: N'

class Triangle(Shape):
    pass

class Square(Shape):
    pass

class Pentagon(Shape):
    pass

class Hexagon(Shape):
    pass