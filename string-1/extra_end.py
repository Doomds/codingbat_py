def extra_end(str):
    return str[-2:]*3

# Tests
print(extra_end('Hello')) # 'lololo'
print(extra_end('ab')) # 'ababab'
print(extra_end('Hi')) # 'HiHiHi'