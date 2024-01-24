p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
total = 0

if p3 < 40 and p4 < 40:
    print("RFF")

if p3 < 40 and p4 >= 40:
    biggest = max(p1,p2,p4)
    smallest = min(p1,p2,p3)
    medium = p1 + p2 + p3 - biggest - smallest
    total += (biggest+medium)/2
    print(round(total))

if p3 >= 40:
    biggest = max(p1,p2,p3)
    smallest = min(p1,p2,p3)
    medium = p1 + p2 + p3 - biggest - smallest
    total += (biggest+medium)/2
    print(round(total))
