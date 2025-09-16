import math
from collections import namedtuple


BaseVector = namedtuple('BaseVector', ['x', 'y'])

# v1 = Vector(3, 5)
# v2 = Vector(13, 15)

# print(v1 + v2)

class Vector(BaseVector):
    __slots__ = () # prevent creation of __dict__ to keet it meory-light

    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)           # Vector(x=3, y=4)
print(abs(v1))      # 5.0
print(v1 + v2)      # Vector(x=4, y=6)
print(v1 * 3)       # Vector(x=9, y=12)
print(bool(v1))     # True
