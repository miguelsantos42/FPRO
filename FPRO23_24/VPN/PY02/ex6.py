hour = int(input())
minute = int(input())
hour = (hour + 6)*60
minute = minute + 51

total_time = hour + minute

total_hours = total_time//60
total_minutes = total_time % 60

if total_hours >= 24:
    total_hours = total_hours - 24

if total_minutes >= 10 and total_hours >= 10:
    print(f"{total_hours}:{total_minutes}")
elif total_minutes < 10 and total_hours >= 10:
    print(f"{total_hours}:0{total_minutes}")
elif total_minutes < 10 and total_hours < 10:
    print(f"0{total_hours}:0{total_minutes}")
else:
    print(f"0{total_hours}:{total_minutes}")

