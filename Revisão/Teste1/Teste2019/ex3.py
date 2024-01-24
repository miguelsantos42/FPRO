n = int(input())
i = 1
linha = ""

for i in range(1,n):
    linha = ""
    for j in range(i):
        linha = linha + str(i) 
    print(linha)