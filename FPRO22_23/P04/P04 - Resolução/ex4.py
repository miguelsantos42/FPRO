def mastermind(g1, g2, g3, c1, c2, c3):
    total = 0
    lista1 = [g1, g2, g3]
    lista2 = [c1,c2,c3]
    for i in range(0, len(lista1)):
        for j in range(0, len(lista2)):
            if (lista1[i] == lista2[j] and i == j):
                total = total + 3
                lista2[j] = "a"
                break
            if (lista1[i] in lista2[j]):
                total = total + 1
                lista2[j] = "l"
                break
    return total

print(mastermind("b", "w", "y", "b", "w", "y"))
print(mastermind("b", "b", "y", "b", "w", "b"))
print(mastermind("b", "w", "y", "w", "y", "w"))
print(mastermind("b", "b", "y", "y", "y", "b"))
