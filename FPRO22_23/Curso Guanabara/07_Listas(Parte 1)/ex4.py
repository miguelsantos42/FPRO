option = 's'
lista = []

while option == 's':
    n = int(input("Digite um valor: "))
    lista.append(n)
    option = str(input("Quer continuar? ")).lower()
    if option == 's':
        continue
    else:
        break
print("-="*30)

print(len(lista))
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado")
