def longest(s):
    lista = s.split()
    longest_word = len(lista[0])
    for i in lista:
        if len(i) > longest_word:
            longest_word = len(i)
    return longest_word

print(longest('A list with some words'))
print(longest('Unnecessarily long sentence since the longest word is the first one'))