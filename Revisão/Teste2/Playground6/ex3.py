def rotate_list(l):
    if(len(l) >= 3):
        return l[3:] + l[:3]
    
print(rotate_list([1, 2, 3, 4, 5, 6]))
print(rotate_list([1, 2, 3, 4, 5, 6, 7, 8]))
print(rotate_list([5, 20, 21, 0, -1, 3]))
print(rotate_list([9, 8, 2]))