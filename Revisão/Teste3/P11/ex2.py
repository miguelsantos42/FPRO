def find_me(f, limits):
    n_guesses = 0
    low, high = limits
    while True:
        n_guesses += 1
        mid = (low+high) // 2
        value = f(mid)
        if value == 0:
            return n_guesses
        if value == -1:
            high = mid - 1
        else:
            low = mid + 1
        

print(find_me(lambda n: -1 if n > 30 else 1 if n < 30 else 0, (0, 100)))
print(find_me(lambda n: -1 if n > 563 else 1 if n < 563 else 0, (-5000, 5000)))
print(find_me(lambda n: -1 if n > -891 else 1 if n < -891 else 0, (-1000, 10000)))
print(find_me(lambda n: 0 if n == 99 else 1, (0, 100)))
