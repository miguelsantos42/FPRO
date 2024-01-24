def longest(s):
    lista = s.split()
    biggest = len(lista[0])
    for i in lista:
        if len(i) > biggest:
            biggest = len(i)
    return biggest

print(longest('A list with some words'))