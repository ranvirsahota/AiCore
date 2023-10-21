import math
class Cylinder():
    def __init__(self, height, radius = 1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()
    
    def get_surface_area(self):
        base_area = 2 * math.pi * (self.radius ** 2)
        lateral_area = (2 * math.pi * self.radius) * self.height
        return round(base_area + lateral_area, 2)
    
    def get_volume(self):
        return round(math.pi * (self.radius ** 2) * self.height, 2)

normal = Cylinder(height = 8, radius = 3)
print(normal.surface_area)
print(normal.volume)