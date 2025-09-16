from collections import abc

print(issubclass(tuple, abc.Sequence))
print(issubclass(tuple, abc.MutableSequence))
print(issubclass(list, abc.MutableSequence))

