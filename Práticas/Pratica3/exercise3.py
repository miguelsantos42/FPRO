n = int(input())

inverso = 0

while(n != 0):
    d = n % 10
    inverso = inverso * 10 + d
    n = n // 10

print(inverso)