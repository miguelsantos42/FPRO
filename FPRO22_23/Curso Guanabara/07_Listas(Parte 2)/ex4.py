matriz = [[0,0,0],[0,0,0],[0,0,0]]
count_even = 0
sum_coloum = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para [{i,j}]: "))
        if matriz[i][j] % 2 == 0:
            count_even = count_even + matriz[i][j]
        if j == 2:
            sum_coloum = sum_coloum + matriz[i][j]

print("-="*30)

for i in matriz:
    for j in i:
        print(f"[{j}]", end="")
    print()
print("-="*30)

print(f"A soma dos valores pares é {count_even}")
print(f"A soma dos valores da terceira coluna é {sum_coloum}")

biggest_line = matriz[1][0]
for i in range(0, 3):
    for j in range(0,3):
        if matriz[1][j] > biggest_line:
            biggest_line = matriz[1][j]
print(f"O maior valor da segunda linha é {biggest_line}")