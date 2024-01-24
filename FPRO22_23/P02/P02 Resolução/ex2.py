n=int(input())
unidades = n % 10
n = n // 10
dezenas = n % 10
n = n // 10
centenas = n % 10
n = n // 10
print(str(n)+'000')
print(str(centenas) + '00')
print(str(dezenas) + '0')
print(str(unidades))
