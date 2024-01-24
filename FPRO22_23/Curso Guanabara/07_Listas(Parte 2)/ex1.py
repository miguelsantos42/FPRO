dados = []
lista = []
option = ""
count = 0
biggest = 0
smallest = 0

nome = str(input("Nome: "))
peso = float(input("Peso: "))
if peso > biggest:
    biggest = peso
smallest = peso
dados.append(nome)
dados.append(peso)
lista.append(dados[:])
dados.clear()
option = str(input("Quer continuar? [S/N]")).lower()
count = count + 1

while option != 'n':
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    if peso > biggest:
        biggest = peso
    if peso < smallest:
        smallest = peso
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
    option = str(input("Quer continuar? [S/N]")).lower()
    count = count + 1

print('-='*20)
print(lista)
print(f"Ao todo, você cadastrou {count} pessoas.")

print(f"O maior peso foi de {biggest}kg. Peso de " ,end = " ")
for i in lista:
    if i[1] == biggest:
            print(f"[{i[0]}]", end=" ")


print(f"\nO menor peso foi de {smallest}kgs. Peso de " ,end = " ")
for i in lista:
    if i[1] == smallest:
        print(f"[{i[0]}]", end=" ")
