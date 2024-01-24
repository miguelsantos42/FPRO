def calc_triangular(n):
    total = 0
    for i in range(0, n+1):
        total = total + i
    return total

print(calc_triangular(1))
print(calc_triangular(3))
print(calc_triangular(10))
print(calc_triangular(23))