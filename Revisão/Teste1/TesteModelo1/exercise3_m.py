from math import pow
from math import factorial

def approx_cos(x, n):
    total = 0
    for k in range(0, n):
        numerador = pow(-1,k)
        denominador = factorial(2*k) 
        total += (numerador/denominador) * pow(x,2*k)
    return(round(total, 5))

