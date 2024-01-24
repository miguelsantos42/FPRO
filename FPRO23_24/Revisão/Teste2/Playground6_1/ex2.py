def nth_lowest(lnum, n):
    lnum.sort()
    return lnum[n-1]

print(nth_lowest([42, 234, 135, 21, 232, 12312, -2343], 2))
print(nth_lowest([73, 100, 23, 18, 84, 61, 56, 75, 92, 38, 54, 73, 3, 13], 12))
print(nth_lowest([9, 8, 2], 1))
print(nth_lowest([73, 100, 23, 18, 84, 61, 56, 75, 92, 38, 54, 73, 3, 13], 14))