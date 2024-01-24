def change(amount):
    lista = []
    while amount>= 200:
        lista.append(200)
        amount -= 200
    while amount>= 100:
        lista.append(100)
        amount -= 100
    while amount >= 50:
        lista.append(50)
        amount -= 50
    while amount >= 20:
        lista.append(20)
        amount -= 20
    while amount >= 10:
        lista.append(10)
        amount -= 10
    while amount >= 5:
        lista.append(5)
        amount -= 5
    while amount>= 2:
        lista.append(2)
        amount -= 2
    while amount >= 1:
        lista.append(1)
        amount -= 1
    
    return lista


# print(change(345))
# print(change(500))
# print(change(17))
# print(change(6))
