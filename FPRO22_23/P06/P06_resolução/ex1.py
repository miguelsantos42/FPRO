def mastermind(guesses, codes):
    corrects = 0
    incorrects = 0

    for p, v in enumerate(guesses):
        for i, j in enumerate(codes):
            if p == i and v == j:
                corrects = corrects + 1
                codes[i] = 'a'
    
    for t in guesses:
        if t in codes:
            incorrects = incorrects + 1
            codes.remove(t)


    return (corrects, incorrects)


print(mastermind(["b", "w", "y"], ["b", "w", "y"]))
print(mastermind(["b", "b", "y"], ["b", "w", "b"]))
print(mastermind(["b", "w", "y"], ["w", "y", "w"]))
print(mastermind(["b", "y"], ["y", "b"]))
