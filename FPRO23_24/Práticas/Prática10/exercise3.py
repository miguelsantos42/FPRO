def pythagoreans(a,b):
    lista = [(x,y,z) for x in range(a, b) for y in range(x+1, b) for z in range(y+1, b) if x*x + y*y == z*z]
    return lista

# print(pythagoreans(1, 10))
# print(pythagoreans(10, 20))
# print(pythagoreans(10, 30))
# print(pythagoreans(51, 91))
