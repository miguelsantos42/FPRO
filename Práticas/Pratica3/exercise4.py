n = int(input())

#impares
if n % 2 != 0:
    for i in range(0, n):
        linha = ''
        for j in range(0, n):
            if ((i == (n-1)//2) and (j == (n-1)//2)):
                linha = linha + '0'
            else:
                linha = linha + '#'
        print(linha) 

#pares
else:
    for i in range(1,n+1):
        linha = ''
        for j in range(1, n+1):
            if((i==(n)//2) and (j==(n)//2)):
                linha = linha + '0'
            elif(i == (n//2)) and (j==(n//2)+1):
                linha = linha + '0'
            elif(i == (n//2)+1 and (j==(n//2))):
                linha = linha + '0'
            elif(i == (n//2)+1 and (j==(n//2)+1)):
                linha = linha + '0'
            else:
                linha = linha + '#'
        print(linha)