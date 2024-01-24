def lista(n):
    if n == 1:
        return [1,1]
    else:
        return [n] + lista(n-1) + [n]