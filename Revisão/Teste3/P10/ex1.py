def square_odds(values):
    num_list = [int(num) for num in values.split(",")]
    square = [str(num**2) for num in num_list if num % 2 != 0]
    return ",".join(square)

print(square_odds("1,2,3,4,5,6,7,8,9"))
print(square_odds("2,4,6,8"))
print(square_odds("115"))
print(square_odds("1,2,3,5,7,11,13"))
