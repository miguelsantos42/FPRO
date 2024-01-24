hours = int(input())
minutes = int(input())

if(hours < 24):
    if(hours == 0):
        if(minutes == 0):
            print('12 am')
        else:
            print(f'{hours}:{minutes} am')    

    elif(hours < 12):
        final_hours = hours
        if(minutes < 60 and minutes > 0):
            final_minutes = minutes
            if(minutes < 10):
                print(f'{final_hours}:0{final_minutes} am')
            else:
                print(f'{final_hours}:{final_minutes} am')
        elif(minutes == 0):
            print(f'{final_hours} am')
        else:
            print("INVALID DATE FORMAT")
    
    elif(hours == 12):
        final_hours = hours
        if(minutes < 60 and minutes > 0):
            final_minutes = minutes
            if(minutes < 10):
                print(f'{final_hours}:0{final_minutes} pm')
            else:
                print(f'{final_hours}:{final_minutes} pm')
        elif(minutes == 0):
            print(f'{final_hours} pm')
        else:
            print("INVALID DATE FORMAT")
    
    else:
        final_hours = hours
        if(minutes < 60 and minutes > 0):
            final_minutes = minutes
            if (minutes < 10):
                print(f'{final_hours-12}:0{final_minutes} pm')
            else:
                print(f'{final_hours-12}:{final_minutes} pm')
        elif(minutes == 0):
            print(f'{final_hours-12} pm')
        else:
            print("INVALID DATE FORMAT")

else:
    print("INVALID DATE FORMAT")


