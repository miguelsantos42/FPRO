def variance(alist):
    media = sum(alist) / len(alist)
    numerador = map(lambda x : (x-media) ** 2, alist)
    final = sum(numerador) / len(alist)
    return round(final, 3)

print(variance([1, 2, 3, 4, 5, 6]))
print(variance([1.5, 2.0, 2.5, 2.0, 1.5]))
print(variance([1, 1, 1, 1, 1]))
print(variance([2, 2, 1, 2, 2]))
