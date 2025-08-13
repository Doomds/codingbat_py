def monkey_trouble(a_smiling, b_smiling):
    if a_smiling and b_smiling:
        return True
    if not a_smiling and not b_smiling:
        return True
    return False


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False)) 