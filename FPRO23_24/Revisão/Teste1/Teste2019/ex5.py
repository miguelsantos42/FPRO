quat = int(input())
power = 0
total = 0

while quat != 0:
    d = quat % 10
    total = total + d * 4 ** power
    quat = quat // 10
    power += 1

print(total)