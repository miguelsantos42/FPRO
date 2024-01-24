def mastermind(g1, g2, g3, c1, c2, c3):
    total = 0
    
    if g1 == c1:
        total += 3
        g1 = -1 
        c1 = 0
    
    if g2 == c2:
        total += 3
        g2 = -1
        c2 = 0

    if g3 == c3:
        total += 3
        g3 = -1
        c3 = 0

    if g1 == c2 or g1 == c3:
        total += 1
        g1 = 0
        c2 = -1
        c3 = -1

    if g2 == c1 or g2 == c3:
        total += 1
        g2 = 0
        c1 = -1
        c3 = -1

    if g3 == c1 or g3 == c2:
        total += 1
        g3 = 0
        c1 = -1
        c2 = -1

    return total


print(mastermind("b", "w", "y", "b", "w", "y"))
print(mastermind("b", "b", "y", "b", "w", "b"))
print(mastermind("b", "w", "y", "w", "y", "w"))
print(mastermind("b", "b", "y", "y", "y", "b"))

    
    
