def x_union(list1,list2):
    el1 = filter(lambda p : p[0] not in
                map(lambda p : p[0], list2),list1)

    el2 = filter(lambda p : p[0] not in 
                map(lambda p: p[0], list1), list2)

    return list(el1) + list(el2)

#print(x_union([('a', 1), ('b', 2), ('c',3)], [('d', 4), ('b', 0)]))
