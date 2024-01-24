def last_man_standing(a_list, step):
    index = 0
    while len(a_list) != 1:
        index = index + step - 1
        while(index >= len(a_list)):
            index = index - len(a_list)
        a_list.pop(index)
    return a_list[0]

print(last_man_standing([3, 4, 1, 6, 2, 5, 7], 3))
print(last_man_standing([6, 3, 8, 2, 1, 8, 5, 2, 2], 10))
print(last_man_standing(['Andre', 'Rui', 'Silva', 'Madalena', 'Leonor', 'Francisco', 'Filomena'], 7))
print(last_man_standing([0.5, -2, 10, 5, 8.9, 10, 20, 10], 3))