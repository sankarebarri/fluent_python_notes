a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(a==b)
x = b
print(x==b)
b[-1].append(99)
print(a==b)
print(x==b)
print(x)
a = a + ('b', 'b')
print(a)
