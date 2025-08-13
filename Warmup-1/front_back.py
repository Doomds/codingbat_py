
def front_back(str):
    if len(str) <= 1:
        return str  # rien à échanger
    return str[-1] + str[1:-1] + str[0]


print(front_back("chat"))
print(front_back("chien"))
print(front_back(""))