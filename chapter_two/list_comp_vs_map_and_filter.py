symbols = '$¢£¥€¤'
beyond_ascii_classique = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii_classique)

beyond_ascii_list_comp = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii_list_comp)