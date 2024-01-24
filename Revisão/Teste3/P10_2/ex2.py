from math import sqrt
def comprehensions(i,j):
    first = [num for num in range(i, j+1) if (num % 10) in (3,8)]
    second = tuple(round(sqrt(num),2) for num in range(i, j+1))
    third = {num : chr(num) for num in range(i, j+1)}
    return (first, second, third)

print(comprehensions(0, 0))
print(comprehensions(100, 102))
print(comprehensions(110, 115))
print(comprehensions(63, 69))
