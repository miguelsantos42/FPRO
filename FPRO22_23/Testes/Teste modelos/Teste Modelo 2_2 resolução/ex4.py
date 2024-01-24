lista = []
def unique_ntree(tree):
    for i in tree:
        if type(i) == int:
            lista.append(i)
        else:
            unique_ntree(i)
    return sorted(set(lista))


#print(unique_ntree((1, (2, (), ()), (1, (), ()))))
#print(unique_ntree((1, (2, (), ()), (4, (6, (), ()), (1, (), ())))))
print(unique_ntree((90, (67, (), (5, (), ())), (4, (), (1, (), (75, (), ()))))))