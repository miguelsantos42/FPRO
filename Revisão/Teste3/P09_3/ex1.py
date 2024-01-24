def differences(alist):
    return list(map(lambda x : x[1] - x[0], zip(alist, alist[1:])))

print(differences([1, 2, 3, 4]))
print(differences([4, 3, 2, 1]))
print(differences([1, 2, 2, 1, 3, 5, 9]))
print(differences([5, 15]))
