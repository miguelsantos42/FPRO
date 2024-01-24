hour  = int(input())
minute = int(input())

if (hour >= 24) or (minute >= 60):
    print("INVALID DATE FORMAT")


elif (hour == 12):
    if(minute == 0):
        print(f"{hour} pm")
    elif(minute > 0 and minute < 10):
        print(f"{hour}:0{minute} pm")
    else:
        print(f"{hour}:{minute} pm")
    

elif (hour > 12):
    hour = hour - 12
    if(minute == 0):
        print(f"{hour} pm")
    elif minute > 0 and minute < 10:
        print(f"{hour}:0{minute} pm")
    else:
        print(f"{hour}:{minute} pm")


if (hour == 0):
    hour = 12
    if(minute == 0):
        print(f"{hour} am")
    elif minute > 0 and minute < 10:
        print(f"{hour}:0{minute} am")
    else:
        print(f"{hour}:{minute} am")

else:
    if(minute == 0):
        print(f"{hour} am")
    elif minute > 0 and minute < 10:
        print(f"{hour}:0{minute} am")
    else:
        print(f"{hour}:{minute} am")


