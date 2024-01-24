def adigits(a,b,c):
    sum = a + b + c
    lowest = min(a,b,c)
    highest = max(a,b,c)
    total = 0
    total = total + lowest*100 + (sum-highest-lowest) * 10 + highest
    return total


