def mastermind(g1, g2, g3, c1, c2, c3):
    guesses = [g1,g2,g3]
    code = [c1,c2,c3]
    total = 0

    for i in range(0, len(guesses)):
        for j in range(0, len(code)):
            if guesses[j] == code[i] and i == j:
                total = total + 3
                code[i] = 'a'
                break
            if guesses[i] in code[j]:
                total = total + 1
                code[j] = 'l'
                break
   
    return total




