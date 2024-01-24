def fib(n):
    lista = []
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        lista.append(0)
        lista.append(1)
        n1 = 0
        n2 = 1
        count = 2
        while count < n:
            nt = n1 + n2
            lista.append(nt)
            n1 = n2
            n2 = nt
            count += 1
        return lista

print(fib(1))
print(fib(5))
print(fib(7))
print(fib(13))