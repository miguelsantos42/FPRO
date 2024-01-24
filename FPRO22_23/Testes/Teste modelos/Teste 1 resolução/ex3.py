from math import factorial
def approx_cos(x,n):
    total = 0
    for i in range(0, n):
        total = total + (((-1)**i) / factorial(2*i) * ((x)**(2*i)))
    return round(total,5)

print(approx_cos(1.0, 3))
print(approx_cos(2.0, 3))
print(approx_cos(1.0, 5))
print(approx_cos(-1.0, 10))
