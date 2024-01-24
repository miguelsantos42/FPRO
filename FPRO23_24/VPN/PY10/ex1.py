def to_celsius(t):
    lista = [round(((num-32)*5)/9,1) for num in t]
    return lista

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))
print(to_celsius([23.0, 28.4, 32.0, 35.6]))
print(to_celsius([]))