symbols = '$¢£¥€¤'
gen_exp = tuple(ord(symbol) for symbol in symbols)
print(gen_exp)

import array
arr = array.array('I', (ord(symbol) for symbol in symbols))
print(arr)
