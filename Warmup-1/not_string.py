def not_string(str):
    if str[0:3] != "not":
        str = "not " + str
        return str
    return str
    
print(not_string('candy')) # 'not candy'
print(not_string('x')) # 'not x'
print(not_string('not bad')) # 'not bad'