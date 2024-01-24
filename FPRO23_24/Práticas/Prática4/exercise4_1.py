def mastermind(g1,g2,g3,c1,c2,c3):
    total  = 0
    if g1 == c1:
        total += 3
        g1 = 'm'
        c1 = 'c'
    
    if g2 == c2:
        total += 3
        g1 = 'm'
        c1 = 'c'

    if g3 == c3:
        total += 3
        g1 = 'm'
        c1 = 'c'

    
    if g1 == c2:
        total += 1
        c2 = 'a'
    
    if g1 == c3:
        total += 1
        c3 = 'g'
        
    
    if g2 == c1:
        total += 1
        c1 = 'a'

    if g2 == c3:
        total += 1
        c3 =  'g'


    if g3 == c1:
        total += 1
        c1 = 'a'
    
    if g3 == c2:
        total += 1
        c2 = 'g'

    return total

print(mastermind("b", "w", "y", "b", "w", "y"))
print(mastermind("b", "b", "y", "b", "w", "b"))
print(mastermind("b", "w", "y", "w", "y", "w"))
print(mastermind("b", "b", "y", "y", "y", "b"))

    
    

    