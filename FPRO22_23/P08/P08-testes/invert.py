def invert(frase):
    if len(frase) == 0:
        return frase
    else:
        return frase[-1] + invert(frase[:-1])