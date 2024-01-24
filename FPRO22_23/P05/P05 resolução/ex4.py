def multi(g):
    res = ()
    for i in range(0, len(g)):
        count = 1
        ref_one, ref_two = g[i]
        for j in range(i + 1, len(g)):
            ref_thi, ref_for = g[j]
            if((ref_one, ref_two) == (ref_thi, ref_for)):
                count = count + 1
        if (ref_one, count, ref_two) not in res:
            res = res + ((ref_one, count, ref_two),) 
        else:
            continue
    return res

print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))
print(tuple(sorted(multi(()))))
print(tuple(sorted(multi(((1,2),(2,3),(3,4))))))
print(tuple(sorted(multi((('A','B'),('B','A'))))))
