def last_man_standing(a_list,step):
    i = 0
    while len(a_list) != 1:
        i = i + step - 1
        while(i >= len(a_list)):
            i = i - len(a_list)
        a_list.pop(i)
    return(a_list)

print(last_man_standing([3, 4, 1, 6, 2, 5, 7], 3))
print(last_man_standing([6, 3, 8, 2, 1, 8, 5, 2, 2], 10))
print(last_man_standing(['Andre', 'Rui', 'Silva', 'Madalena', 'Leonor', 'Francisco', 'Filomena'], 7))
print(last_man_standing([0.5, -2, 10, 5, 8.9, 10, 20, 10], 3))

