# Première Solution
def last2(str):
    if len(str) < 2:
        return 0

    last2_chars = str[-2:]

    number_of_occurence = 0
    i = 0
    while i < (len(str)-2):
        i_substring = str[i:i+2]
        
        if last2_chars == i_substring:
            number_of_occurence += 1
        
        i += 1

    return number_of_occurence

# Solution refactorisée avec un for
def last2_with_for(str):
    if len(str) < 2:
        return 0
    
    last2_chars = str[-2:]
    number_of_occurence = 0

    for i in range(len(str)-2):
        i_substring = str[i:i+2]

        if last2_chars == i_substring:
            number_of_occurence += 1
    
    return number_of_occurence

# Test
print(last2('hixxhi')) # 1
print(last2('xaxxaxaxx')) # 1
print(last2('axxxaaxx')) # 2

print(last2_with_for('hixxhi')) # 1
print(last2_with_for('xaxxaxaxx')) # 1
print(last2_with_for('axxxaaxx')) # 2