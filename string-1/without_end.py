def without_end(str):
    first = str[1:]
    return first[:-1]

# Tests
print(without_end('Hello')) # 'ell'
print(without_end('java')) # 'av'
print(without_end('coding')) # 'odin'