def min_path(path):
    
    dir_opositte = {
        'UP':'DOWN',
        'DOWN':'UP',
        'LEFT':'RIGHT',
        'RIGHT':'LEFT'
    }

    percurso = path[:]
    i = 0

    while i < len(percurso)-1:
        actual_path = percurso[i]
        next_path = percurso[i+1]

        if dir_opositte[actual_path] == next_path:
            del percurso[i:i+2]
            i += 1
        else:
            i +=1
    
    return percurso


print(min_path(['UP', 'DOWN', 'UP', 'LEFT', 'RIGHT']))
print(min_path(['UP', 'LEFT', 'DOWN', 'RIGHT']))
print(min_path(['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']))
