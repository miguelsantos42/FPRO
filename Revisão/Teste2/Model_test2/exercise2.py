def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def next_prime(number):
    n = number + 1
    while(not is_prime(n)):
        n += 1
    return n


print(next_prime(10))
print(next_prime(13))
print(next_prime(26))
print(next_prime(450))
