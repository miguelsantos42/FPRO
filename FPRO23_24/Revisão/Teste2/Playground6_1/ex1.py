def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        new_list = []
        new_list.append(0)
        new_list.append(1)
        n0 = 0
        n1 = 1
        i = 2
        while i < n:
            soma = n0 + n1
            new_list.append(soma)
            n0 = n1
            n1 = soma
            i += 1
    return new_list

print(fib(1))
print(fib(5))
print(fib(7))
print(fib(13))