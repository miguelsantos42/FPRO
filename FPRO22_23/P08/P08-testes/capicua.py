def capicua(frase):
    if len(frase) == 0 or len(frase) == 1:
        return True
    elif capicua[0] == capicua[-1]:
        return capicua(frase[1:-1])
    else:
        return False
    
        