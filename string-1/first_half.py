def first_half(str):
    half = int(len(str) / 2)
    return str[:half]
    

# Tests
print(first_half('WooHoo')) # 'Woo'
print(first_half('HelloThere')) # 'Hello'
print(first_half('abcdef')) # 'abc'