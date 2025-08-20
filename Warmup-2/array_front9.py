def array_front9(nums):
    if nums[:4].count(9):
        return True
    return False

# Tests

print(array_front9([1, 2, 9, 3, 4])) # True
print(array_front9([1, 2, 3, 4, 9])) # False
print(array_front9([1, 2, 3, 4, 5])) # False