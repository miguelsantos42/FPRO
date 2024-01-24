def dict2list(adict, m, n):
    final_mat = []
    for i in range(0, m):
        lista = []
        for j in range(0, n):
            lista.append(adict.get((i,j), 0))
            adict.pop((i,j), 0)
        final_mat.append(lista)
    if len(adict) == 0:
        return final_mat
    return None



print(dict2list({(0, 1): 4, (2, 1): 6}, 2, 3))
print(dict2list({(0, 1): 4, (1, 2): 6}, 2, 3))
print(dict2list({(0, 1): 4, (2, 1): 6}, 5, 5))
print(dict2list({(0, 0): 35, (1, 1): 20, (1, 4): 10, (2, 2): 7, (2, 5): 67, (3, 2): 99, (3, 5): -20}, 4, 6))
