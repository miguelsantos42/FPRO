n = int(input())
total = 0

for i in range(1, n+1):
    if (i % 3 == 0) or (i % 5 == 0) or(i % 3 == 0 and i % 5 == 0):
        total = total + i

print(total)
