def dict2list(adict, m, n):
    lista = []
    for i in range(m):
        lista_choosen = []
        for j in range(n):
            lista_choosen.append(adict.get((i,j),0))
            adict.pop((i,j),0)
        lista.append(lista_choosen)
    if len(adict) == 0:
        return lista
    else:
        return None
    

print(dict2list({(0, 1): 4, (2, 1): 6}, 2, 3))
print(dict2list({(0, 1): 4, (1, 2): 6}, 2, 3))
print(dict2list({(0, 1): 4, (2, 1): 6}, 5, 5))
print(dict2list({(0, 0): 35, (1, 1): 20, (1, 4): 10, (2, 2): 7, (2, 5): 67, (3, 2): 99, (3, 5): -20}, 4, 6))
