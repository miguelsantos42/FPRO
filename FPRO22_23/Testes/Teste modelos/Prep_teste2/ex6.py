def mastermind(guesses, codes):
    correct = 0
    incorrect = 0
    for i, p in enumerate(guesses):
        for k, l in enumerate(codes):
            if i == k and p == l:
                correct = correct + 1
                codes[k] = "a"

                
    for j in guesses:
        if j in codes:
            incorrect = incorrect + 1
            codes.remove(j)


    return (correct, (correct + incorrect)- correct)


print(mastermind(["b", "w", "y"], ["b", "w", "y"]))
print(mastermind(["b", "b", "y"], ["b", "w", "b"]))
print(mastermind(["b", "w", "y"], ["w", "y", "w"]))
print(mastermind(["b", "y"], ["y", "b"]))

            