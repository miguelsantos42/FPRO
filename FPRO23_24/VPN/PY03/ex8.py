import math

total = 0

for k in range(0, 50):
    numerador = ((math.factorial(4*k)) * (1103 + 26390*k))
    denominador = ((math.factorial(k))**4)*(396**(4*k))
    total = total + (numerador / denominador)
total = total * ((2*math.sqrt(2))/9801)
final = 1 / total
print(round(final,8))

