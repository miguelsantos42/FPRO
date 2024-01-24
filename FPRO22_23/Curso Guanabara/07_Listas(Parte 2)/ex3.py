matriz = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para [{i, j}]: "))
        
print(matriz)
print("-="*30)

for i in matriz:
    for j in i:
        print(f"[{j}]", end = "")
    print()