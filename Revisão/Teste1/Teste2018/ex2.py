d = int(input())
num = int(input())

total = 0

while num != 0:
    p = num % 10
    if p > d:
        total = total + (2*p)
        num = num // 10
    else:
        num = num // 10

print(total)
