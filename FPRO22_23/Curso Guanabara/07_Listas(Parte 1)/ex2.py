option = 's'
lista = []

while option == 's':
    n = int(input("Digite um valor: "))
    if n not in lista:
        print("Valor adicionado com sucesso...")
        lista.append(n)
    else:
        print("Valor duplicado! Não vou adicionar...")
    option = str(input("Quer continuar? ")).lower()
    if option == 's':
        continue
    else:
        break
print("-="*30)
lista.sort()
print(f"Você digitou os valores {lista}")
