tupla_numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                 'seis', 'sete', 'oito', 'nove', 'dez',
                 'onze', 'doze', 'treze', 'catorze', 'quinze',
                 'dezasseis', 'dezassete', 'dezoito', 'dezanove',
                 'vinte')

choice = int(input("Digite um número entre 0 e 20: "))
while (choice < 0) or (choice > 20):
    print("Tente novamente.", end=" ")
    choice = int(input("Digite um número entre 0 e 20: "))
print(f"Você digitou o número {tupla_numeros[choice]}")
