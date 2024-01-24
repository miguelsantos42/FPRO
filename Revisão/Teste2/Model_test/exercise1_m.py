def time_diff(time1, time2):
    time = (time1[0]*60 + time1[1]) - (time2[0] * 60 + time2[1])
    time = abs(time)
    return (time // 60, time % 60)

# print(time_diff((14, 30), (17, 45)))
# print(time_diff((10, 25), (10, 20)))
# print(time_diff((19,30), (17, 00)))
# print(time_diff((10, 45), (10, 45)))

