expression = str(input())

lista = []

for i in expression:
    if i == "(":
        lista.append(i)
    elif i == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break

if len(lista) == 0:
    print("A sua expressão está válida")
else:
    print("A sua expressão está inválida!")

