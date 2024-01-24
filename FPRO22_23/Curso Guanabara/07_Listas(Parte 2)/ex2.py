lista = []
lista_pares = []
lista_impares = []

for i in range(0,7):
    n = int(input(f"Digite o {i+1}o. valor: "))
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

lista_pares = sorted(lista_pares)
lista_impares = sorted(lista_impares)


lista.append(lista_pares[:])
lista_pares.clear()
lista.append(lista_impares[:])
lista_impares.clear()


print(f"A lista completa foi: {lista}")
print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores impares digitados foram: {lista[1]}")
