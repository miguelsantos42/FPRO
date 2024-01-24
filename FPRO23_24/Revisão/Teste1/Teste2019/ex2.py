d = int(input())
num = int(input())

total = 0

while num != 0:
    if (num % 10 > d):
        total += pow(num%10,2)
        num = num // 10
    else:
        num = num // 10

print(total)