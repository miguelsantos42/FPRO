n = int(input())

if(n % 2 != 0):
    for i in range(0,n):
        linha = ""
        for coluna in range(0,n):
            if((i == (n-1)//2) and (coluna == (n-1)//2)):
                linha = linha + '0'
            else:
                linha = linha + '#'
        print(linha)

else:
    for i in range(1,n+1):
        linha = ""
        for coluna in range(1, n+1):
            if (i == n//2) and (coluna == n//2):
                linha = linha + '0'
            elif (i == (n//2)+1) and (coluna == (n//2)+1):
                linha = linha + '0'
            elif (i == (n//2) + 1) and (coluna == n//2):
                linha = linha + '0'
            elif(i == (n)//2) and (coluna == (n//2) + 1):
                linha = linha + '0'
            else:
                linha = linha + '#'
        print(linha)