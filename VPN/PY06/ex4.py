def bagdiff(xs,ys):
    lista = []
    for i in xs:
        if i in ys:
            ys.remove(i)
            continue
        else:
            lista.append(i)
    return lista

print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))
print(bagdiff([5, 7, 11, 11, 11, 12, 13], []))
print(bagdiff([], [7, 8, 11]))