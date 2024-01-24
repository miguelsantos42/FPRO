dec = int(input())
total = 0
power = 0

while(dec):
    d = dec % 8
    total += d * 10 ** power
    dec = dec // 8
    power += 1

print(total)
