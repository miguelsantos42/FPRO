def bissect(f,n):
    low = 0
    up = 1
    for _ in range(n):
        mid = (low + up) / 2
        if(f(low)*f(up)) > 0:
            low = mid
            up = mid
        