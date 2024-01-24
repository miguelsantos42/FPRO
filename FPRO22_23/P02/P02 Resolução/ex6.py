p = int(input())
r = float(input())/100
n = int(input())
t = 2

total = float(p*(1+(r/n))**(n*t))

print(round(total,3))
