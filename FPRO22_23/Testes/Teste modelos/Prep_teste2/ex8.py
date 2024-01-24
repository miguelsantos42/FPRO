def local_minima(alist):
    final_list = []
    for i in range(0, len(alist)-2):
        lista_choosen = alist[i:i+3]
        lista_choosen.sort()
        if lista_choosen[0] != lista_choosen[1]:
            final_list.append(lista_choosen[0])
    return final_list 


print(local_minima([10, 3, 3, 14, 5, 7, 4]))
print(local_minima([0, 3, 3, 14, 5, 7, 4]))
print(local_minima([2, 1, 1, 1, 7, 3, 1]))
print(local_minima([5, 1, 43, 21, 5, 63, 1, 5, 5, 5]))
