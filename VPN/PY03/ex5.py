n = int(input())

aux = n 
new = 0
final = 0
count = 0

while aux != 0:
    d = aux % 10
    new = new * 10 + d
    count = count + 1
    aux = aux // 10
    

while new != 0:
    for i in range(count-1, -1, -1):
        d = new % 10
        final = final + d * (8**i)
        new = new // 10   

print(final)