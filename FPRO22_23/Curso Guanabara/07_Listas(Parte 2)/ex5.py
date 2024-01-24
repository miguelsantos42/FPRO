from time import sleep
from random import randint

print("-"*30)
print("JOGA NA MEGA SENA")
print("-"*30)

jogos = int(input("Quantos jogos você quer que eu sorteie? "))
lista = []
q = 1

print("-="*3, end=" ")
print(f"SORTEANDO {jogos} JOGOS", end=" ")
print("-="*3, end="")

print()

while q <= jogos:
    lista_choose = []
    cont = 0
    while True:
        j = randint(1,60)
        if j not in lista_choose:
            lista_choose.append(j)
            cont = cont + 1
        if cont >= 6:
            break
    lista_choose.sort()
    lista.append(lista_choose[:])
    lista_choose.clear()
    q = q + 1

p = 1 
for i in lista:
    sleep(1)
    print(f"Jogo {p}: {i}")
    p = p + 1
    

print("-="*4,end="")
print("< BOA SORTE! >",end=" ")
print("-=" *4, end="")
print()


