a = int(input())
b = int(input())

while a < b and a ** 2 <= (b / 2) ** 2:
    n = a
    if a % 3 != 0 and a % 5 != 0:
        if a % 2 == 0:
            n //= 2
            n //= 2
            n //= 2
        else:
            n += 1
        print(n)
    a += 3

