n = int(input())

a = n % 10
n = n // 10
b = n % 10
n = n // 10
c = n % 10
n = n // 10
d = n % 10
n = n // 10

print(f"unidade: {a}")
print(f"dezena: {b}")
print(f"centena: {c}")
print(f"milhar: {d}")


