n = int(input())
count = 0
new = 1

while n > 9:
    aux = n
    while aux != 0:
        new *= (aux % 10) 
        aux = aux // 10
    n = new
    if n > 9:
        count += 1
    else:
        continue

print(count)