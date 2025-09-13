def sum3(nums):
    total = 0
    for num in nums:
        total += num
    return total
    
# Tests
print(sum3([1, 2, 3])) # 6
print(sum3([5, 11, 2])) # 18
print(sum3([7, 0, 0])) # 7