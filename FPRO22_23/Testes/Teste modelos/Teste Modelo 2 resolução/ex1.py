def leap_year(y):
    if(y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def next_leap_year(y):
    next_one = y + 1
    while not leap_year(next_one):
        next_one = next_one + 1
    return next_one

print(next_leap_year(2004))
print(next_leap_year(2000))
print(next_leap_year(2021))
print(next_leap_year(12346))
