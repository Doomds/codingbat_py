def diff21(n):
    if n > 21:
        return abs((21-n)*2)
    return abs(21-n)

print(diff21(22))   # 2
print(diff21(25))    # 8
print(diff21(30))   # 18
print(diff21(50))   # 58