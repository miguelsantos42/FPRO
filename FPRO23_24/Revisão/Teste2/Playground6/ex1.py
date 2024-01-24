def fib(n):
    lista = []
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        n0 = 0
        n1 = 1
        lista.append(0)
        lista.append(1)
        count = 2
        while count <= n:
            soma = n0 + n1
            lista.append(soma)
            n0 = n1
            n1 = soma
            count += 1
        return lista

print(fib(1))
print(fib(5))
print(fib(7))
print(fib(13))
