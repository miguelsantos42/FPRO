def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def primes_difference(n):
    smallest = n 
    biggest = n + 1 
    while not (is_prime(smallest)):
        smallest = smallest - 1
    while not(is_prime(biggest)):
        biggest = biggest + 1
    return biggest - smallest

print(primes_difference(74))
print(primes_difference(60))
print(primes_difference(10))
print(primes_difference(193))
