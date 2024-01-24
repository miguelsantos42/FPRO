from math import sqrt
def comprehensions(i, j):
    alist = [num for num in range(i,j+1) if num % 10 in (3,8)]
    atuple =  tuple(round(sqrt(num),2) for num in range(i, j+1))
    adict = {x : chr(x) for x in range(i, j+1)} 
    return (alist, atuple, adict)

# print(comprehensions(0, 0))
# print(comprehensions(100, 102))
# print(comprehensions(110, 115))
# print(comprehensions(63, 69))
