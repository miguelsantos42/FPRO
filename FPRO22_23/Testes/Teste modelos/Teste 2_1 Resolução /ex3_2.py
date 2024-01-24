def total_distance(dist, cities):
    if not cities:
        return 0  # If the list of cities is empty, return 0
    total = 0
    for i in range(len(cities) - 1):
        # Check if there is a direct connection between consecutive cities
        if (cities[i], cities[i + 1]) in dist:
            total += dist[(cities[i], cities[i + 1])]
        elif (cities[i+1], cities[i]) in dist:
            total += dist[(cities[i+1], cities[i])]
        else:
            return -1  # If there is no connection, return -1
    return total


print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Lisboa']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Viseu','Coimbra']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Lisboa', 'Coimbra']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Lisboa','Coimbra','Porto','Braga','Vigo']))
