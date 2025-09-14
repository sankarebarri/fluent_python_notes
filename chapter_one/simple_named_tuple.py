def simple_namedtuple(type_name, field_names):
    # Create the __init__ method dynamically
    def __init__(self, *args):
        for name, value in zip(field_names, args):
            setattr(self, name, value)

    # Create the __repr__ method for nice printing
    def __repr__(self):
        values = ', '.join(f"{name}={getattr(self, name)!r}" for name in field_names)
        return f"{type_name}({values})"
    
    # Create the new calss with type()
    cls = type(type_name, (object,), {
        '__init__':__init__,
        '__repr__': __repr__,
        '_fields': tuple(field_names)
    })
    return cls

Point = simple_namedtuple('Point', ['x', 'y'])

p = Point(3, 7)
print(p)
print(p.x)