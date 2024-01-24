def dogs(h_age):
    total = 0
    if h_age > 2:
        total = total + 2 * 10.5
        h_age = h_age - 2
        total = total + h_age * 4
    else:
        total = total + h_age * 10.5
    return total


print(dogs(1))
print(dogs(2))
print(dogs(4))