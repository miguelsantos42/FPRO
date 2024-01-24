def is_pair_of_square(number_one, number_two):
    if number_one == number_two:
        return False
    
    square_one = number_one * number_one
    square_two = number_two * number_two

    aux = square_two
    final_aux = 0
    while aux != 0:
        d = aux % 10
        final_aux = final_aux * 10 + d
        aux = aux // 10

    if square_one == final_aux:
        return True
    else:
        return False
    
    
print(is_pair_of_square(13, 31))
print(is_pair_of_square(24, 42))
print(is_pair_of_square(103, 301))
print(is_pair_of_square(111, 111))
