def lfsr(n):
    original = n
    phrase = ""

    while True:
        first = str(int(n[-1])^int(n[-2]))
        phrase += n[-1]

        n = n[:-1]
        n = first + n

        if n == original:
            break
    
    return phrase
