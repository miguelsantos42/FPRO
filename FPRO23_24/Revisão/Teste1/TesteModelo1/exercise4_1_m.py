def proper_divisors_sum(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.extend([i, n // i])
    return sum(divisors)

def check_friendly(number_one, number_two):
    if number_one == number_two:
        return f'identical numbers: {number_one}'
    
    sum_divisors_one = proper_divisors_sum(number_one)
    sum_divisors_two = proper_divisors_sum(number_two)
    
    if sum_divisors_one != number_two or sum_divisors_two != number_one:
        return f'sum of divisors of {number_one} is not {number_two}'
    else:
        return f'{number_one} and {number_two} are friendly'

# Test cases
print(check_friendly(77, 77))  # Output: identical numbers: 77
print(check_friendly(12, 55))  # Output: sum of divisors of 12 is not 55
print(check_friendly(18, 21))  # Output: sum of divisors of 21 is not 18
print(check_friendly(220, 284))  # Output: 220 and 284 are friendly