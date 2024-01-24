def min_path(path):
    new_list = []

    opp = {
        'UP'  : 'DOWN',
        'DOWN': 'UP',
        'LEFT': 'RIGHT',
        'RIGHT': 'LEFT'
    }

    i = 0

    while i < len(path) - 1:
        actual_path = path[i]
        next_path = path[i+1]

        if(opp[actual_path] == next_path):
            i += 1
            del (path[i:i+2])
            continue
        else:
            new_list.append(actual_path)
            i += 1
    
    if i == len(path)-1:
        new_list.append(path[-1])

    return new_list

print(min_path(['UP', 'DOWN', 'UP', 'LEFT', 'RIGHT']))
print(min_path(['UP', 'LEFT', 'DOWN', 'RIGHT']))
print(min_path(['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']))
