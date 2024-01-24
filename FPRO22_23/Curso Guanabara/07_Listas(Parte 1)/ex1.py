lista = []

for i in range(0, 5):
    n = int(input(f"Digite um valor na Posição {i}: "))
    lista.append(n)


print("-="*20)

print(f"Você digitou os valores {lista}")

biggest = lista[0]
smallest = lista[0]
for i in range(0,5):
    if lista[i] > biggest:
        biggest = lista[i]
    if lista[i] < smallest:
        smallest = lista[i]

print(f"O maior valor digitado foi {biggest} nas posições ", end=" ")
for p, v in enumerate(lista):
    if v == biggest:
        print(f"{p}...", end=" ")


print(f"\nO menor valor digitado foi {smallest} nas posições ", end=" ")
for p, v in enumerate(lista):
    if v == smallest:
        print(f"{p}...", end=" ")
print()
