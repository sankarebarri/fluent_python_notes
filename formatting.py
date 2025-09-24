# The format specifier syntax in the f-string is:
# {value:[fill][align][sign][#][0][width][,][_][.precision][type]}

# Width and Alignment
word = 'hi'
print(f'{word:10}')
print(f'{word:<10}')
print(f'{word:>10}')
print(f'{word:^10}')

# Fill character
number = '42'
print(f'{number:0>5}')
print(f'{number:*<5}')
print(f'{number:+^6}')

n = 42
# Signs for number
print(f'{n:+}')
print(f'{-n:+}')

# Precision and floating point
fl = 12345.6789
print(f'{fl:.2f}')
print(f'{fl:.1f}')
1.2346e+04
123,456,789
123_456_789

print(f'{fl:.4e}') # 1.2346e+04

# Number and grouping
num = 123456789
print(f'{num:,}') # 123,456,789
print(f'{num:_}') # 123_456_789

# Percentages
print(f'{0.12:.2%}')

data = [("Alice", 25, 91.5), ('Bob', 30, 88.234)]
print(f'{"Name":10} | {"Age":^5} | {"Score":>8}')
print('-'*30)
for name, age, score, in data:
    print(f'{name:10} | {age:^5d} | {score:8.2f}')
