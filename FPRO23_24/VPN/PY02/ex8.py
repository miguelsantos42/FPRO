a = int(input())
b = int(input())

diff = a + b + ((a-b)%2) * (a*b)

print(diff)