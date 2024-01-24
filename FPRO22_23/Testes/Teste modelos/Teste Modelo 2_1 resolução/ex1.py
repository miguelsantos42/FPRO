def is_leap(y):
    if y % 4 == 0 and(y % 100 != 0 or y % 400 == 0):
        return True
    return False


def next_leap_year(y):
    y = y + 1
    while not is_leap(y):
        y = y + 1
    return y

print(next_leap_year(2004))
print(next_leap_year(2000))
print(next_leap_year(2021))
print(next_leap_year(12346))

