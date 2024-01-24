import math
def raiz(a,b,c):
    return math.sqrt(pow(b,2) - 4 * a * c)

def for_pos(a,b,c):
    return (-b + raiz(a,b,c))/(2*a)

def for_neg(a,b,c):
    return (-b - raiz(a,b,c))/(2*a)

def solver(a,b,c):
    lista = []
    d = pow(b,2) - 4 * a * c
    if d > 0:
        lista.append(for_pos(a,b,c))
        lista.append(for_neg(a,b,c))
        return sorted(lista)
    elif d == 0:
        lista.append(for_pos(a,b,c))
        return lista
    else:
        return lista

print(solver(2,5,-3))
print(solver(-2,-5,-3))
print(solver(-10,1,-10))

