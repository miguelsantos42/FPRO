def count(a,b,g):
    count = 0
    for x, y in g:
        if a == x and b == y:
            count += 1
    return count


def multi(g):
    tup = ()
    for first, second in g:
        tot = count(first, second, g)
        if (first, tot, second) not in tup:
          tup += (first, tot, second),
    return tup

print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))
print(tuple(sorted(multi(()))))
print(tuple(sorted(multi(((1,2),(2,3),(3,4))))))
print(tuple(sorted(multi((('A','B'),('B','A'))))))
