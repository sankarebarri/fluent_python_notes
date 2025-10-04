invoice = """
...
0.....6.................................40........52...55........
... 1909 Pimoroni PiBrella
$17.50      3
$52.50
... 1489 6mm Tactile Switch x20
$4.95
2
$9.90
... 1510 Panavise Jr. - PV-201
$28.00
1
$28.00
... 1601 PiTFT Mini Kit 320x240
$34.95
1
$34.95
... """

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]
print(line_items)
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

l[3::2] = [11, 22]
print(l)

# l[2:5] = 100 # error,the R.H must be an iterable
l[2:5] = [100]

l = [1, 2]
a = l * 5
b = 5 * l
print(b)
print(a)
print(l)
y = 'abcd'
5 * y
print(y)

t = (1, 2, [30, 40])
# t[2] += [50, 60]
print(t)

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(id(fruits))
# print(fruits.sort())
print(id(fruits))
sorted(fruits)
print(id(fruits))

print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, reverse=True, key=len))

