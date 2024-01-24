def time_diff(time1, time2):
    lista1 = []
    lista2 = []
    for i in range(0, len(time1)):
        if type(time1[i]) == int:
            lista1.append(time1[i])

    for j in range(0, len(time2)):
        if type(time2[j]) == int:
            lista2.append(time2[j])

    hour1 = lista1[0]
    hour2 = lista2[0]
    minute1 = lista1[1]
    minute2 = lista2[1]
    
    if hour1 > hour2:
        hour = hour1 - hour2
        if minute1 > minute2:
            minute = minute1 - minute2
        elif minute1 < minute2:
            minute = minute2 - minute1
        else:
            minute = minute1 - minute2
    elif hour1 < hour2:
        hour = hour2 - hour1
        if minute1 > minute2:
            minute = minute1 - minute2
        elif minute1 < minute2:
            minute = minute2 - minute1
        else:
            minute = minute1 - minute2
    elif hour1 == hour2:
        hour = hour1 - hour2
        if minute1 > minute2:
            minute = minute1 - minute2
        elif minute1 < minute2:
            minute = minute2 - minute1
        else:
            minute = minute1 - minute2
    return(hour, minute)

print(time_diff((14, 30), (17, 45)))
print(time_diff((10, 25), (10, 20)))
print(time_diff((19,30), (17, 00)))
print(time_diff((10, 45), (10, 45)))
