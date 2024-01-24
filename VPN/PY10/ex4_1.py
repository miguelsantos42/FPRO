def evaluate(a, x):
    return sum((a[i]*(x**i) for i in range(0, len(a))))

print(evaluate([1, 2, 4], 5))
print(evaluate([1, 2, 4], 10))
print(evaluate([1, 2, 4, 6, 8], 2))
print(evaluate([1, 2, 4, 6, 8], -2))