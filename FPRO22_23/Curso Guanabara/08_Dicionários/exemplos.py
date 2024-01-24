'''pessoas = {'nome' : 'Gustavo', 'Sexo' : 'M', 'idade':  22}
pessoas['peso'] = 98.5
for k,v in pessoas.items():
    print(f'{k} = {v}')
'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem o valor {v}")

