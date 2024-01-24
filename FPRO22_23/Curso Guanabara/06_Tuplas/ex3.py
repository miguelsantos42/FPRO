from random import randint  

n1 = randint(1,10)
n2 = randint(1,10)
n3 = randint(1,10)
n4 = randint(1,10)
n5 = randint(1,10)

tupla = (n1,n2,n3,n4,n5)

print("Os valores sorteados foram: ", end = " ")
for i in tupla:
    print(i, end = " ")
print(f"\no maior valor sorteado foi {max(tupla)}")
print(f"o menor valor sorteado foi {min(tupla)}")

