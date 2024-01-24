def check_friendly(number_one, number_two):
    total_one = 0
    total_two = 0

    for i in range(1,number_one):
        if number_one % i == 0:
            total_one += i
    
    for j in range(1,number_two):
        if number_two % j == 0:
            total_two += j

    if number_one == number_two:
        return(f"identical numbers: {number_one}")
    else:
        if total_one != number_two and total_two != number_one:
            return(f"sum of divisors of {number_one} is not {number_two}")
        elif total_one == number_two and total_two != number_one:
            return(f"sum of divisors of {number_two} is not {number_one}")
        elif total_one != number_two and total_two == number_one:
            return(f"sum of divisors of {number_one} is not {number_two}")
        else:
            return(f"{number_one} and {number_two} are friendly")


# print(check_friendly(77, 77))
# print(check_friendly(12, 55))
# print(check_friendly(18, 21))
# print(check_friendly(220, 284))
