num = int(input())

if (num % 2 != 0):
    for i in range(0, num):
        linha = ''
        for j in range(0, num):
            if (num % 2 != 0):
                if(i == (num//2) and j == (num//2)):
                    linha = linha + '0'
                else:
                    linha = linha + '#'
        print(linha)
        
else:
    for i in range(1, num+1):
        linha = ''
        for j in range(1, num+1):
            if((i == (num//2) and j == (num//2))):
                linha = linha + '0'
            elif ((i == (num//2)+1) and (j == (num//2))):
                linha = linha + '0'
            elif ((i == (num//2)) and (j==(num//2)+1)):
                linha = linha + '0'
            elif ((i == (num//2)+1) and (j==(num//2)+1)):
                linha = linha + '0'
            else:
                linha = linha + '#'
        print(linha)
    
            
