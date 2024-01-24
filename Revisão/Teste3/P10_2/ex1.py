def square_odds(values):
    lista_num = [int(num) for num in values.split(",")]
    lista_impares = [str(x * x) for x in lista_num if x % 2 != 0]
    return ",".join(lista_impares)

print(square_odds("1,2,3,4,5,6,7,8,9"))
print(square_odds("2,4,6,8"))
print(square_odds("115"))
print(square_odds("1,2,3,5,7,11,13"))

