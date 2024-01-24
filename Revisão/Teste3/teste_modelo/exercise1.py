def days_until_christmas(date):

    days_of_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    number_of_days = 0
    
    day, month , year = date
    
    if 25 > day:
        number_of_days += 25 - day
    elif day > 25:
        if month < 12:
            number_of_days += days_of_month[month] - day + 25
            month += 1
        elif month == 12:
            number_of_days += days_of_month[month] - day + 25
            month = 12 - 11

    
    while month < 12:
        number_of_days += days_of_month[month]
        month += 1

    return number_of_days

print(days_until_christmas((18, 12, 2022)))
print(days_until_christmas((25, 12, 2022)))
print(days_until_christmas((26, 12, 2022)))
print(days_until_christmas((10, 1, 2023)))


