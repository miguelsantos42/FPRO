def bagdiff(xs,ys):
    new_list = []
    for i in xs:
        if i in ys:
            ys.remove(i)
            continue
        else:
            new_list.append(i)
    return new_list

print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))
print(bagdiff([5, 7, 11, 11, 11, 12, 13], []))
print(bagdiff([], [7, 8, 11]))