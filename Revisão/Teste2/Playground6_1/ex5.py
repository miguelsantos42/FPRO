def fetch_middle(llist):
    lista = []
    for i in llist:
        if(len(i) % 2 != 0):  #impar
            lista.append(i[len(i)//2])
        else:                 #par
            n = len(i)
            media = (i[n//2-1] + i[(n//2)])/2
            lista.append(media)
    return lista

print(fetch_middle([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]))
print(fetch_middle([[10, 25, 35, 45], [100, -1, 3, 4], [-3, -5, -10, -20, -100]]))
print(fetch_middle([[1]]))
