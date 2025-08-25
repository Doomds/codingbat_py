def non_start(a, b):
    if len(a) < 1 or len(b) < 1:
        return ""
    return a[1:] + b[1:]

# Tests
print(non_start('Hello', 'There')) # 'ellohere'
print(non_start('java', 'code')) # 'avaode'
print(non_start('shotl', 'java')) # 'hotlava'