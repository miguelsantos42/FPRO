def local_minima(alist):
    new_list = []
    for i in range(0, len(alist)-2):
        choosen_list = alist[i:i+3]
        choosen_list.sort()
        if choosen_list.count(choosen_list[0]) == 1:
            new_list.append(choosen_list[0])
    return new_list

print(local_minima([10, 3, 3, 14, 5, 7, 4]))
print(local_minima([0, 3, 3, 14, 5, 7, 4]))
print(local_minima([2, 1, 1, 1, 7, 3, 1]))
print(local_minima([5, 1, 43, 21, 5, 63, 1, 5, 5, 5]))
