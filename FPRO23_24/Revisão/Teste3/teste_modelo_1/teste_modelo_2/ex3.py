def lfsr(n):

    original = n
    phrase = ""

    while True:
        first = str(int(n[-2]) ^ int(n[-1]))
        phrase += n[-1]

        n = n[:-1]
        n = first + n

        if n == original:
            break

    return phrase

print(lfsr('100'))
print(lfsr('10'))
print(lfsr('1010'))
print(lfsr('10101'))

