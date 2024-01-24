def check_friendly(number_one, number_two):
    total_1 = 0
    total_2 = 0

    if number_one == number_two:
        return(f"identical numbers: {number_one}")
    else:
        for i in range(1, number_one):
            if number_one % i == 0:
                total_1 += i
        
        for j in range(1, number_two):
            if number_two % j == 0:
                total_2 += j

        if total_1 == number_two and total_2 == number_one:
            return(f"{number_one} and {number_two} are friendly")
        else:
            return(f"sum of divisors of {number_one} is not {number_two}")
        

print(check_friendly(77, 77))
print(check_friendly(12, 55))
print(check_friendly(21, 18))
print(check_friendly(220, 284))
