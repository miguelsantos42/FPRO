def mult(M,N):
    if(len(M[0]) != len(N)):
        return ()
    
    final = []

    for i in range(0, len(M)):
        lista = []
        for j in range(0, len(N[0])):
            a = 0
            for k in range(0, len(N)):
                a =  a  +  (M[i][k] * N[k][j])
            lista = lista + [a]
        final = final + [lista,]
    return final

print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
print(mult([[1, 2, 3], [4, 5, 6]], [[9], [8], [7]]))
print(mult([[7, 8, 9, 10]], [[5], [3], [2], [7]]))
print(mult([[1, 2], [3, 4]], [[5], [6], [7]]))

