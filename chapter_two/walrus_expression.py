x = 'ABC'
codes = [ord(x) for x in x]
print(codes)

codes_walrus = [last := ord(c) for c in x]
print(codes_walrus)
print(last)