def total_distance(dist, cities):
    if len(cities) == 0 or len(cities) == 1:
        return 0
    
    total_distance = 0

    for i in range(0, len(cities)-1):
        cities_choose = (cities[i], cities[i+1])
        #distance = dist.get(cities_choose, None)
        for k,v in dist.items():
            if v is None:
                return -1
            total_distance+=v
    return total_distance


print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Lisboa']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Viseu','Coimbra']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Lisboa', 'Coimbra']))
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Lisboa','Coimbra','Porto','Braga','Vigo']))
