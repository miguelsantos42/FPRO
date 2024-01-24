def fetch_middle(llist):
    new_list = list()
    for i in llist:
        n = len(i)
        #len impar
        if n % 2 != 0:
            new_list.append(i[(n)//2])
        else:
            media = (i[n//2] + i[(n//2)-1])/2
            new_list.append(media)
    return new_list


print(fetch_middle([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]))
