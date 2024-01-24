def reversed(lista):
    return lista[::-1]

def pattern_hunting(l1,l2,p):
    new_list = []
    for i in range(0, len(l1)):
        val1 = l1[i]
        val2 = l2[i]
        if p in val1 and p not in val2:
            new_list.append(val2)
        if p in val2 and p not in val1:
            new_list.append(val1)
    
    new_list.sort()

    return reversed(new_list)
    

print(pattern_hunting(['a string', 'two strings', 'not here'], ['choose me', 'me too', 'but not me'], 'string'))
print(pattern_hunting(['not found', 'pattern here', 'skip', 'next... or not?'], ['pattern here indeed', 'i want to be chosen', 'not my day', 'sneakypatternbutitisthere'], 'pattern'))