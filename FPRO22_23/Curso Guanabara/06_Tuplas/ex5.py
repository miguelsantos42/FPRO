listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-'*50)
print(' '*16,end="")
print("LISTAGEM DE PREÇOS",end="")
print()
print('-'*50)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}')
    else:
        print(f'{listagem[pos]:.>0}')
print('-'*50)