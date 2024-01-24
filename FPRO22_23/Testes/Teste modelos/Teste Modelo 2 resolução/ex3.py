def dict2list(adict,m,n):
    
    lista = list()
    for i in range(0, m):
        lista_choose = []
        for j in range(0, n):
            lista_choose.append(adict.get((i,j), 0))
            adict.pop((i,j), None)
        lista.append(lista_choose)
    if len(adict) == 0:
        return lista
    return None
    

print(dict2list({(0, 1): 4, (2, 1): 6}, 2, 3))
print(dict2list({(0, 1): 4, (1, 2): 6}, 2, 3))
print(dict2list({(0, 1): 4, (2, 1): 6}, 5, 5))
print(dict2list({(0, 0): 35, (1, 1): 20, (1, 4): 10, (2, 2): 7, (2, 5): 67, (3, 2): 99, (3, 5): -20}, 4, 6))
