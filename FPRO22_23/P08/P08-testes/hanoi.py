def hanoi(n,a,b,c):
    if n == 1: #Caso base
        print(f"Move-se o disco {n} de {a} para {c}")
    else:
        hanoi(n-1,a,c,b)
        print(f"Move-se o disco {n} de {a} para {c}")
        hanoi(n-1,b,a,c)


print(hanoi(3,'Principio', 'Meio', 'Fim'))