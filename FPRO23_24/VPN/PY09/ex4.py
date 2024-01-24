def evaluate(a,x):
    total = map(lambda i, p : p * (x ** i), a)
    return sum(total)


print(evaluate([1, 2, 4], 5))
print(evaluate([1, 2, 4], 10))
print(evaluate([1, 2, 4, 6, 8], 2))
print(evaluate(	[1, 2, 4, 6, 8], -2))