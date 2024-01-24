option = 's'
lista = []
lista_par = []
lista_impar = []

while option == 's':
    n = int(input("Digite um valor: "))
    lista.append(n)
    option = str(input("Quer continuar? ")).lower()
    if option == 's':
        continue
    else:
        break
print("-="*30)

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)



print(lista)
print(lista_par)
print(lista_impar)
