from math import factorial
def compute_euler(n):
    total = 0
    for i in range(0, n+1):
        total = total + (1/factorial(i))
    return round(total, 5)

print(compute_euler(50))
print(compute_euler(5))
print(compute_euler(0))
print(compute_euler(1))


