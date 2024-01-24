def multi(g):
    tup = []

    for i in g:
        contador = g.count(i)
        if ((i[0], contador, i[1])) not in tup:
            tup.append((i[0], contador, i[1]),)
    
    return tuple(tup)

print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))
print(tuple(sorted(multi(()))))
print(tuple(sorted(multi(((1,2),(2,3),(3,4))))))
print(tuple(sorted(multi((('A','B'),('B','A'))))))
