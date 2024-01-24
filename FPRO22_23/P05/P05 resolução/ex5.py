def triplet(tup):
    for i in range(0, len(tup)-2):
        for j in range(1, len(tup)-1):
            for k in range(2, len(tup)):
                if (tup[i] + tup[j] + tup[k] == 0):
                    return (tup[i], tup[j], tup[k])
    return ()

print(triplet((-8, 0, 4, -2, -1, 1, 2)))
print(triplet((-1, 1, 1, 1)))
print(triplet((-4, 3, 0, -2, -1, -3)))
print(triplet((-1, 0, -5, -2, 4, 5, 15, 21, 42, 3)))
