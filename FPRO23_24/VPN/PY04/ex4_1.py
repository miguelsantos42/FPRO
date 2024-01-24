import math
def raiz(a,b,c):
    return math.sqrt(pow(b,2) - 4 * a * c)

def for_pos(a,b,c):
    return (-b + raiz(a,b,c))/(2*a)

def for_neg(a,b,c):
    return (-b - raiz(a,b,c))/(2*a)

def solver(a,b,c):
    lista = []
    lista.append(for_pos(a,b,c))
    lista.append(for_neg(a,b,c))
    sorted(lista)
    return lista


print(solver(2,5,-3))
print(solver(-2,-5,-3))
