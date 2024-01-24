from math import sqrt
def comprehensions(i, j):
    first = [n for n in range(i, j+1) if n % 10 in (3,8)]
    second = tuple(round(sqrt(x),2) for x in range(i, j+1))
    third = {n : chr(n) for n in range(i,j+1)}
    return(first,second,third)

print(comprehensions(0, 0))
print(comprehensions(100, 102))
print(comprehensions(110, 115))
print(comprehensions(63, 69))
