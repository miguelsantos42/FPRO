def local_minima(alist):
    lista = []
    lista_choose = []
    for i in range(0, len(alist)-2):
        lista_choose = alist[i:i+3]
        lista_choose.sort()
        if (lista_choose[0] != lista_choose[1]):
            lista.append(lista_choose[0])
    return lista

print(local_minima([10, 3, 3, 14, 5, 7, 4]))
print(local_minima([0, 3, 3, 14, 5, 7, 4]))
print(local_minima([2, 1, 1, 1, 7, 3, 1]))
print(local_minima([5, 1, 43, 21, 5, 63, 1, 5, 5, 5]))
