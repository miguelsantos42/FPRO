def mastermind(guesses,codes):
    correct = 0
    incorrect = 0

    for x, y in enumerate(guesses):
        for pos, val in enumerate(codes):
            if x == pos and y == val:
                correct += 1
                val = 'a'
    
    for i in guesses:
        if i in codes:
            incorrect += 1
            i = 'p'
    
    return (correct, incorrect-correct)



print(mastermind(["b", "w", "y"], ["b", "w", "y"]))
print(mastermind(["b", "b", "y"], ["b", "w", "b"]))
print(mastermind(["b", "w", "y"], ["w", "y", "w"]))
print(mastermind(["b", "y"], ["y", "b"]))


