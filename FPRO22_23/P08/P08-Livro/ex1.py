def div(dividendo,divisor):
    if divisor > dividendo:
        return dividendo
    else:
        return div(dividendo - divisor, divisor)
    

print(div(10,3))
