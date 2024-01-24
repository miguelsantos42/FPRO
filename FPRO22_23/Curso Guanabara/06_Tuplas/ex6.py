palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

vogais = ('a', 'e', 'i', 'o', 'u')


for i in palavras:
    print(f"Na palavra {i.upper()} temos", end=" ")
    for j in i:
        if j in vogais:
            print(f"{j}", end=" ")
    print()
