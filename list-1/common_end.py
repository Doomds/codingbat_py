def common_end(a, b):
    if len(a) >= 1 and len(b) >= 1:
        if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
            return True
    return False


# Tests
print(common_end([1, 2, 3], [7, 3])) # True
print(common_end([1, 2, 3], [7, 3, 2])) # False
print(common_end([1, 2, 3], [1, 3])) # True