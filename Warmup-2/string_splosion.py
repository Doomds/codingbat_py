
# Prendre la première lettre 
# ensuite rajouter les deux premières 
# ensuite rajouter les 3 premières 
# et ainsi de suite.

def string_splosion(str):
    
    length = len(str)
    
    new_str = ""
    i = 0 
    while i < length:
        char = str[:i+1]
        new_str += char
        i += 1

    return new_str


# Test
print(string_splosion("Code")) # 'CCoCodCode'
print(string_splosion("abc"))  # 'aababc'
print(string_splosion("ab"))   # 'aab'