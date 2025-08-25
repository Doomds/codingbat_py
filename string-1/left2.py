def left2(str):
    if len(str) < 2:
        return ""
    return str[2:] + str[:2]

# Test
print(left2('Hello')) # 'lloHe'
print(left2('java')) # 'vaja'
print(left2('Hi')) # 'Hi'