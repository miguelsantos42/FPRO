def max_path(tree):
    if type(tree) == int:
        return tree
    elif type(tree) == tuple:
        (left, value, right) = tree
        return max(max_path(left) + value, max_path(right) + value)
    


print(max_path(((2, 1, ((1, 2, 2), 2, 1)), 0, (5, 4, 2))))
print(max_path((1, 3, 2)))
print(max_path(((1, 1, 3), 0, 3)))
print(max_path(((2, 3, (4, 5, 2)), 0, (7, 1, 3))))
