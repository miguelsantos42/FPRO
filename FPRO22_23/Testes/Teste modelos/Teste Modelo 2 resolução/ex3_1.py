def dict2list(adict, m, n): 
    mat = []
    for i in range(m):
        line = []
        for j in range(n):
            line.append(adict.get((i, j), 0))
            adict.pop((i, j), None)
        mat.append(line)
    if len(adict) == 0:
        return mat
    return None

print(dict2list({(0, 1): 4, (2, 1): 6}, 2, 3))
print(dict2list({(0, 1): 4, (1, 2): 6}, 2, 3))
print(dict2list({(0, 1): 4, (2, 1): 6}, 5, 5))
print(dict2list({(0, 0): 35, (1, 1): 20, (1, 4): 10, (2, 2): 7, (2, 5): 67, (3, 2): 99, (3, 5): -20}, 4, 6))
