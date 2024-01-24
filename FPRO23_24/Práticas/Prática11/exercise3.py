def search_tree(key, tree):
    visited = []
    current_node = tree
    while current_node is not None:
        (k,v,left,right) = current_node
        visited.append(key)
        if k == key:
            return (v, visited)
        if k < key:
            current_node = right
        if k > key:
            current_node = left
    return None

# print(search_tree('apple', ('banana', 2, ('apple', 1, None, None), ('pear', 5, None, None))))
# print(search_tree('banana', ('banana', 2, ('apple', 1, None, None), ('pear', 5, None, None))))
# print(search_tree('coconut', ('banana', 2, ('apple', 1, None, None), ('pear', 5, None, None))))
