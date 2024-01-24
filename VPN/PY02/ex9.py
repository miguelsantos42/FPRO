a = int(input())
b = int(input())

total_50 = 0
total_20 = 0
total_10 = 0
total_5 = 0

exchange = b - a

while exchange >= 50:
    exchange -= 50
    total_50 += 1
while exchange >= 20:
    exchange -= 20
    total_20 += 1
while exchange >= 10:
    exchange -= 10
    total_10 += 1
while exchange >= 5:
    exchange -= 5
    total_5 += 1

print(f"{total_50} {total_20} {total_10} {total_5}")
