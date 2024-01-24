def occupied(reservations, limit):
    count = 0
    for i in reservations:
        for j in range(i[0],i[1]+1):
            if j <= limit:
                count+=1
    return count


print(occupied([(1,2), (7,8), (12,13)], 10))
print(occupied([(1,5), (7,10)], 3))
print(occupied([(1,1), (3,10)], 7))
print(occupied([(0,2), (4,5), (7,10)], 10))

