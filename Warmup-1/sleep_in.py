def sleep_in(weekday, vacation):
    if weekday == True and vacation == True:
        return True
    if weekday == False and vacation == True:
        return True
    if weekday == False and vacation == False:
        return True
    
    return False


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))