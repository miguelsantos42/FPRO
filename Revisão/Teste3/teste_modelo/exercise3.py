def lfsr(n):
    original = n
    phrase = ""

    while True:
        new_digit = str(int(n[-2]) ^ int(n[-1]))
        phrase += n[-1] #0
        
        n = n[:-1] #10
        n = new_digit + n

        if n == original:
            break

    return phrase

print(lfsr('100'))
print(lfsr('10'))
print(lfsr('1010'))
print(lfsr('10101'))

