from math import factorial
from math import pow
def approx_cos(x, n):
    total = 0
    for k in range(0,n):
        numerador = pow(-1,k)
        denominador = factorial(2*k)
        total += (numerador/denominador) * pow(x,2*k)
    return(round(total,5))


# print(approx_cos(1.0, 3))
# print(approx_cos(2.0, 3))
# print(approx_cos(1.0, 5))
# print(approx_cos(-1.0, 10))
