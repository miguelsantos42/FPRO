hour = int(input())
minute = int(input())

if hour >= 24 or minute >= 60:
    print("INVALID DATE FORMAT")
else:
    if hour >= 12:
        suffix = "pm"
    else:
        suffix = "am"

    if hour == 0:
        if minute == 0:
            print(f"12 am")
        else:
            if minute > 0 and minute < 10:
                print(f"{hour}:0{minute} {suffix}")
            else:
                print(f"{hour}:{minute} {suffix}")

    elif hour < 12:
        if minute > 0 and minute < 10:
            print(f"{hour}:0{minute} {suffix}")
        else:
            print(f"{hour}:{minute} {suffix}")

    elif hour == 12:
        if minute == 0:
            print(f"12 pm")
        else:
            if minute > 0 and minute < 10:
                print(f"{hour}:0{minute} {suffix}")
            else:
                print(f"{hour}:{minute} {suffix}")

    else:
        if minute > 0 and minute < 10:
            print(f"{hour-12}:0{minute} {suffix}")
        else:
            print(f"{hour-12}:{minute} {suffix}")

