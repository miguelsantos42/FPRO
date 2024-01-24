golos = []
count = 0
nome = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas Joelson jogou? "))
for i in range(0, partidas):
    golo = int(input(f"Quantos golos na partidas {i}? "))
    golos.append(golo)
    count = count + golo

print("-="*30)
jogador = {'nome' : nome, 'golos': golos, 'total': count}
print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print('-='*30)
print(f"O jogador {jogador['nome']} jogou {partidas}")
for i in range(0, len(golos)):
    print(f"   => Na partida {i}, fez {golos[i]}")
print(f"Foi um total de {jogador['total']} golos")
