n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

tupla = (n1,n2,n3,n4)

print(f"O número 9 apareceu {tupla.count(9)} vezes ")

if 3 in tupla:
    print(f"o 3 foi digitado na posição {tupla.index(3)+1}")
else:
    print("O número 3 não foi digitado!")

count = 0
for i in tupla:
    if i % 2 == 0:
        count  = count + 1 

if count == 0:
    print("Não existem valores pares!")
else:
    print("Os valores pares digitados foram:", end= " ")
for i in tupla:
    if i % 2 == 0:
        print(i, end = " ")
    


