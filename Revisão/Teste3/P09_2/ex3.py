def x_union(list1, list2):
    lista1 = filter(lambda x : x[0] not in map(lambda p : p[0], list2), list1)
    lista2 = filter(lambda x : x[0] not in map(lambda p : p[0], list1), list2)
    return list(lista1) + list(lista2)

print(x_union([('a', 1), ('b', 2), ('c',3)], [('d', 4), ('b', 0)]))
print(x_union([('a', 1), ('b', 2)], [('b', 3), ('a', 4)]))
print(x_union([('b', 1), ('a', 2)], [('c', 3), ('d', 4)]))
print(x_union([('a', 'b'), ('b', 'c')], [('b', 'b'), ('c', 'b')]))

