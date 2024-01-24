def map(pos, steps):
    x = pos[0]
    y = pos[1]
    lista = steps.split('-')
    
    for i in lista:
        if i == "up":
            y += 1
        elif i == "down":
            y -= 1
        elif i == "left":
            x -= 1
        else:
            x += 1
        
    return (x,y)


print(map((0, 0), 'up-up-left-right-up-up'))
print(map((0, 4), 'up-up-left-left-up-up'))
print(map((0, 0), 'down-left-down-left-up-right-right-up'))
print(map((8, 4), 'down-down-left-left-up-up'))