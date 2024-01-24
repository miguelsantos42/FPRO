from random import randint
from time import sleep

jogadores = {'jogador1': randint(1,6),
             'jogador2': randint(1,6),
             'jogador3': randint(1,6),
             'jogador4': randint(1,6)}

for k,v in jogadores.items():
    print(f"O jogador {k} tirou o {v}")
    sleep(1)

posicao = 1
print("")

for i in sorted(jogadores, key = jogadores.get, reverse=True):
    print(f"{posicao}ºlugar: {i} com {jogadores[i]}")
    posicao = posicao + 1
    sleep(1)