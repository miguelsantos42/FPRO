def check_hamming(number):
    aux = number
    count_5 = 0
    count_3 = 0
    count_2 = 0

    while (aux % 2 == 0):
        count_2 = count_2 + 1
        aux = aux // 2
    while (aux % 3 == 0):
        count_3 = count_3 + 1
        aux = aux // 3
    while (aux % 5 == 0):
        count_5 = count_5 + 1
        aux = aux // 5

    if aux == 1:
        return f"{number} is 2^{count_2}*3^{count_3}*5^{count_5}"
    else:
        return f"{number} is not Hamming"
    
print(check_hamming(60))
print(check_hamming(27))
print(check_hamming(26))
print(check_hamming(450))

