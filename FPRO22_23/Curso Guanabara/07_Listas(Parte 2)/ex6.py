lista = []
aux = []

nome = str(input())
nota1 = float(input())
nota2 = float(input())
media = (nota1 + nota2)/2
lista.append(nome)
lista.append(media)
aux.append(lista[:])
lista.clear()
option = str(input("Quer continuar? [S/N]"))

while option != 'n':
    nome = str(input())
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1 + nota2)/2
    lista.append(nome)
    lista.append(media)
    aux.append(lista[:])
    lista.clear()
    option = str(input("Quer continuar? [S/N]"))

print("-="*30)

print("No. Nome         MÉDIA")
print("-"*30)
for p, v in enumerate(aux):
    print(f"{p} {v[0]}            {v[1]:>8.1f}")
print("-"*30)

#decision = 0
#while decision != 999:

    