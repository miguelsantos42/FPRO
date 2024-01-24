def time_diff(time1, time2):
    minutes1 = time1[0] * 60 + time1[1]
    minutes2 = time2[0] * 60 + time2[1]

    time_diff = abs(minutes1-minutes2)

    hour = time_diff // 60
    minutes = time_diff % 60

    return(hour, minutes)

print(time_diff((14, 30), (17, 45)))
print(time_diff((10, 25), (10, 20)))
print(time_diff((19,30), (17, 00)))
print(time_diff((10, 45), (10, 45)))
