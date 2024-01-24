def change(money):

    coins = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    dici = {}

    for i in coins:
        count = int(money // i)
        dici[i] = count
        money -= (i * count)

    return dici


print(change(5))
print(change(5.23))
print(change(7.71))
print(change(4.45))
