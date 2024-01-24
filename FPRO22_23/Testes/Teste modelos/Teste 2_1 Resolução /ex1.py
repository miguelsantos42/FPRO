def time_diff(time1, time2):
    time_first = time1[0] * 60 + time1[1]
    time_second = time2[0] * 60 + time2[1]

    #diferença de tempos em minutos
    time_diff = max(time_first, time_second) - min(time_first, time_second)

    hours = time_diff // 60
    minutes = time_diff % 60

    return(hours, minutes)


print(time_diff((14, 30), (17, 45)))
print(time_diff((10, 25), (10, 20)))
print(time_diff((19,30), (17, 00)))
print(time_diff((10, 45), (10, 45)))
