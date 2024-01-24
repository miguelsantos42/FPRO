p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())

if p3 < 40 and p4 < 40:
    print("RFF")
else:
    if p3 < 40:
        highest = max(p1,p2,p4)
        lowest = min(p1,p2,p4)
        medium = p1 + p2 + p4 - highest - lowest
        print((highest + medium)//2)
    else:
        highest = max(p1,p2,p3)
        lowest = min(p1,p2,p3)
        medium = p1 + p2 + p3 - highest - lowest
        print((highest + medium)//2)
    