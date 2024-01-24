def flatten(alist):
    if len(alist) == 0:
        return []
    elif type(alist[0]) == list:
        return flatten(alist[0]) + flatten(alist[1:]) 
    else:
        return [alist[0]] + flatten(alist[1:])

print(flatten([]))
print(flatten(['Hello', [2, [[], False]], [True]]))
print(flatten([[1,[2,3]], [4,[[5]],6], [7,8,9]]))
print(flatten([1]))
