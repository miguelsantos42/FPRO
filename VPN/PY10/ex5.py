def rearranges(l):
    negative = [i for i in l if i <= 0]
    positive = [j for j in l if j > 0]
    return negative + positive

print(rearranges([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))
print(rearranges([-19, -15, -14, -9, -18, -1, -4]))
print(rearranges([]))
print(rearranges([-3, 3, -5, 0, 7, 13, -1]))

