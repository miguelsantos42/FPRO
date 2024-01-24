def sum_numbers(number):
    total = 0
    for i in range(1, number):
        total = total + i
    return total

def average(number):
    total = 0
    count = 0
    for i in range(1, number+1):
        total = total + i
        count = count + 1
    return (total/count)


def var_numbers(number,precision = 2):
    total = 0
    for i in range(1, number+1):
        total = total + ((i-average(number))**2)
    final = total / number
    return (round(final, precision))


#print(var_numbers(3))
#print(var_numbers(10, 1))
#print(var_numbers(15, 3))
#print(var_numbers(7))
