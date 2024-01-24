aluno = dict()
nome = str(input("Nome: "))
media = float(input(f"Média de {nome}: "))
aluno = {'nome': nome, 'media': media}
print(f'Nome é igual a {nome}')
print(f'Média é igual a {media}')
if media < 5:
    print("Situação é igual a Reprovado")
if media >= 5 and media < 7:
    print("Situação é de Recuperação") 
if media >= 7:
    print("Situação é igual a Aprovado")
