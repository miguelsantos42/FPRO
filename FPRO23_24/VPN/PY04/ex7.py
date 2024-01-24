def collatz(n):
    string = ""
    aux = n
    string = string + str(n)
    while aux != 1:
        if aux % 2 != 0:
            string += ',' + str(aux * 3 +1) 
            aux = aux * 3 + 1
        else:
            string += ',' +str(aux // 2)
            aux = aux // 2
    return string

print(collatz(3))
