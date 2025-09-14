from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(3, 7)

print(p)
print(p.x)
print(p.y)
print(isinstance(p, tuple))

# Exploring the Class
print(Point.__name__)
print(Point._fields)
print(Point.__base__)
print(Point.__bases__)

# See all it's built-in methods
print(dir(p))

# namedtuple behaves like a tupe meaning:
# It can be unpacked, indexed, etc
a, b = p
print(a ,b)
print(p[0] ,p[1])

# Using namedtuple gives you:
    # clean, concise code
    # Automatic __init__, __repr__, __eq__
    # Both tuple-like behaviour and object like access
    # Immutable and memory-efficient(unlike full classes)

