p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())

if(p3 < 40):
    if(p4 < 40):
        print("RFF")
    else:
        if(p1 > p2 and p4 >= p2):
            media = (p1 + p4)/2
            print(round(media))
        elif(p2 > p1 and p4 >= p1):
            media = (p2 + p4)/2
            print(round(media))
        else:
            media = (p1 + p2)/2
            print(round(media))
else:
    if(p1 > p2 and p3 >= p2):
        media = (p1 + p3)/2
        print(round(media))
    elif(p2 > p1 and p3 >= p1):
        media = (p2 + p3)/2
        print(round(media))
    else:
        media = (p1+p2)/2
        print(round(media))