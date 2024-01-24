def mastermind(guesses,code):
    correct = 0
    incorrect = 0

    for i in range(0, len(guesses)):
        if guesses[i] == code[i]:
            correct += 1
            code[i] = 'a'


    for k in guesses:
        if k in code:
            incorrect += 1
            code.remove(k)
    
    return (correct, incorrect)


# print(mastermind(["b", "w", "y"], ["b", "w", "y"]))
# print(mastermind(["b", "b", "y"], ["b", "w", "b"]))
# print(mastermind(["b", "w", "y"], ["w", "y", "w"]))
# print(mastermind(["b", "y"], ["y", "b"]))

