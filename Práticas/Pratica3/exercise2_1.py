hour = int(input())
minute = int(input())

if hour not in range(0,24) or minute not in range(0,60):
    print("INVALID DATE FORMAT")
else:
    if hour < 12:
        suffix = "am"
    else:
        suffix = "pm"

    if hour == 0:
        hour = 12

    elif hour > 12:
        hour = hour - 12

    if minute == 0:
        print(f"{hour} {suffix}")
    else:
        print(f"{hour}:{minute:02} {suffix}")
        
