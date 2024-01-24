n = int(input())

a = n % 10
n = n // 10
b = (n % 10) * 10
n = n // 10
c = (n % 10) * 100
n = n // 10
d = (n % 10) * 1000
n = n // 10

print(f"{d}\n{c}\n{b}\n{a}")

