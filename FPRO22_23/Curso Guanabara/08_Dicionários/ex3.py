dici = {}
nome = str(input("Nome: "))
born = int(input("Ano de Nasciemnto: "))
ctps = int(input("Carteira de trabalho (0 não tem): "))
if ctps != 0:
    hire = int(input("Ano de contratação: "))
    salary = int(input("Salário: R$ "))
    dici = {'nome' : nome, 'idade' : 2023 - born, 'ctps' : ctps,
            'contratação' : hire, 'salário' : salary, 'reforma' : (hire - born)+35}
    print("-="*40)
    print(dici)
    for k, v in dici.items():
        print(f"{k} tem o valor de {v}")
else:
    dici = {'nome' : nome, 'idade' : 2023 - born, 'ctps' : ctps}
    print(dici)
    for k, v in dici.items():
        print(f"{k} tem o valor de {v}")