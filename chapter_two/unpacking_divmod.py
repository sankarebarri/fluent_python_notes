t = divmod(20, 8)
print(t)
a, b = t
print(a, b)

quotient, remainder = divmod(*t)
print(quotient, remainder)

import os

path, file_name = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(path, file_name)

# parallell assignement
a, b, *rest = range(5) #
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body)

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print(fun(*[1,2], *[3, 4], 5, 6, 7, 8, 9))
print(fun(*[1,2], *[3, 4], *range(5)))

print(range(5), 5)
print(*range(5), 5)
print({*range(4), 4, *(5, 6, 7)}) # set literals

