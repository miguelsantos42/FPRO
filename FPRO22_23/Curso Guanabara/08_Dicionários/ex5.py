lista = []
nome = str(input("Nome: ")).capitalize()
sexo = str(input("Sexo: ")).upper()
idade = int(input("Idade: "))
count = 1
idade_total = idade
pessoas = {'nome' : nome, 'idade' : idade, 'sexo': sexo}
lista.append(pessoas)
option = str(input("Quer continuar? ")).lower()

while option != 'n':
    nome = str(input("Nome: ")).capitalize()
    sexo = str(input("Sexo: ")).upper()
    idade = int(input("Idade: "))
    count = count  + 1
    idade_total = idade_total + idade
    pessoas = {'nome' : nome, 'idade' : idade, 'sexo': sexo}
    lista.append(pessoas)
    option = str(input("Quer continuar? ")).lower()

print("-="*30)
print(f"O grupo tem {count} pessoas")
print(f"A média tem {idade_total / count} pessoas")

print("As mulheres cadastradas foram: ",end="")
for k in lista:
    if k['sexo'] == 'F':
        print(f"{k['nome']}",end=" ")
    
print()
print("Lista de pessoas que estão acima da média:")
media_total = idade_total / count
for pessoa in lista:
    if pessoa['idade'] > media_total:
        print("nome:", pessoa['nome'], end="; ")
        print("idade:", pessoa['idade'], end="; ")
        print("sexo:", pessoa['sexo'],end="; ")
        print()
print("<< ENCERRADO >> ")
