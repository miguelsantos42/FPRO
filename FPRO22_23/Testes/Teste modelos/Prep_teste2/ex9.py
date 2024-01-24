def magic(mat):
    reference = sum(mat[0])

    #linhas
    for i in range(0, len(mat)):
        if sum(mat[i]) != reference:
            return False
        
    #colunas
    total = 0
    for j in range(0, len(mat)):
        total = 0
        for k in range(0, len(mat)):
            total = total + mat[k][j]
        if total != reference:
            return False
    
    #diagonal esquerda
    total_a = 0
    for l in range(0, len(mat)):
        for m in range(0, len(mat)):
            if l == m:
                total_a = total_a + mat[l][m]
    if total_a != reference:
        return False   

    #diagonal direita
    total_b = 0
    matt = []
    for z in mat:
        matt.append(z[::-1])
    for n in range(0, len(matt)):
        for o in range(0, len(matt)):
            if n == o:
                total_b = total_b + matt[n][o]
    if total_b != reference:
        return False
    
    return True


print(magic([[8, 1, 6], [3, 5, 7], [4, 9, 2]]))
print(magic([[8, 1, 6], [3, 6, 7], [4, 9, 2]]))
print(magic([[16, 2, 12], [6, 10, 14], [8, 18, 4]]))
print(magic([[8, 3, 4], [1, 5, 9], [6, 7, 2]]))
print(magic([[9, 1, 6], [3, 6, 7], [4, 9, 3]]))
print(magic([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]]))
print(magic([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [5, 7, 14, 21, 23], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]]))
print(magic([[17, 24, 2, 8, 15], [23, 5, 8, 14, 16], [4, 6, 14, 20, 22], [10, 12, 20, 21, 3], [11, 18, 26, 2, 9]]))
print(magic([[16, 2, 12], [6, 10, 14], [8, 18, 4]]))
print(magic([[34, 48, 2, 16, 30], [46, 10, 14, 28, 32], [8, 12, 26, 40, 44], [20, 24, 38, 42, 6], [22, 36, 50, 4, 18]]))
print(magic([[18, 24, 1, 8, 15], [23, 6, 7, 14, 16], [4, 6, 14, 20, 22], [10, 12, 19, 22, 3], [11, 18, 25, 2, 10]]))
print(magic([[17, 24, 1, 8, 16], [23, 5, 7, 15, 16], [4, 6, 14, 20, 22], [10, 13, 19, 21, 3], [12, 18, 25, 2, 9]]))
print(magic([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [5, 7, 14, 21, 23], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]]))
print(magic([[17, 24, 2, 8, 15], [23, 5, 8, 14, 16], [4, 6, 14, 20, 22], [10, 12, 20, 21, 3], [11, 18, 26, 2, 9]]))
print(magic([[1, 1, 1], [0, 0, 0], [2, 2, 2]]))
print(magic([[1, 1, 1], [1, 2, 0], [1, 0, 2]]))
print(magic([[1, 0, 2], [1, 0, 2], [1, 0, 2]]))

