def count_until(tup):
    count = 0
    for i in tup:
        if type(i) == tuple:
            return count
        count += 1
    return -1

print(count_until((1, '2', 3, 4.0, 5j)))
print(count_until((1, 2, (3,), 4.0, 5j)))
print(count_until(()))
print(count_until((1, 2, 6, 4.0, ())))