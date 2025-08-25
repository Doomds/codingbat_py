def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    if len(a) > len(b):
        return b + a + b
    else:
        return ""

# Tests
combo_string('Hello', 'hi') # 'hiHellohi'
combo_string('hi', 'Hello') # 'hiHellohi'
combo_string('aaa', 'b') # 'baaab'