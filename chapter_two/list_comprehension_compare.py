symbols = '$¢£¥€¤'
codes_list = []
for symbol in symbols:
    codes_list.append(ord(symbol))

print(codes_list)

codes_comp = [ord(symbol) for symbol in symbols]
print(codes_comp)