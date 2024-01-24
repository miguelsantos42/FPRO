def total_distance(dist, cities):
    total = 0

    for i in range(1, len(cities)):
        if (cities[i-1], cities[i]) in dist:
            total = total + dist[cities[i-1], cities[i]]
        elif (cities[i], cities[i-1]) in dist:
            total = total + dist[cities[i], cities[i-1]]
        else:
            return -1
        
    return total


print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Lisboa']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Viseu','Coimbra']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Lisboa', 'Coimbra']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Lisboa','Coimbra','Porto','Braga','Vigo']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto']))
