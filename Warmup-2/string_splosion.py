
# Prendre la première lettre 
# ensuite rajouter les deux première 
# ensuite rajouter les 3 première 
# et ainsi de suite.

def string_splosion(str):
    
    length = len(str)
    
    new_str = ""
    i = 0 
    while i < length:
        char = str[:i]
        new_str += char
        i += 1

    return new_str


# Test
print(string_splosion("Code")) # 'CCoCodCode'
print(string_splosion("abc"))  # 'aababc'
print(string_splosion("ab"))   # 'aab'