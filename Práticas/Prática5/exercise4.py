def count(a,b,g):
    res = 0
    for x,y in g:
        if a == x and b == y:
            res += 1
    return res


def multi(g):
    tup = ()
    for first, second in g:
        n = count(first, second,g)
        if (first, n, second) not in tup:
            tup += ((first, n, second),)
        else:
            continue
    return tup
        

# print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))
# print(tuple(sorted(multi(()))))
# print(tuple(sorted(multi(((1,2),(2,3),(3,4))))))
# print(tuple(sorted(multi((('A','B'),('B','A'))))))
