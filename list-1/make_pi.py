import math

def make_pi():
    array = []
    pi = math.pi
    one = int(pi)
    two = int((pi * 10)-30)
    three = int((pi * 100) - 310)
    
    array.append(one)
    array.append(two)
    array.append(three)
    
    return array

print(make_pi())