def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0

    for i in range(shorter-1):
        a_substring = a[i:i+2]
        b_substring = b[i:i+2]
        if a_substring == b_substring:
            count += 1
    
    return count
    

# Tests
print(string_match('xxcaazz', 'xxbaaz')) # 3
print(string_match('abc', 'abc')) # 2
print(string_match('abc', 'axc')) # 0