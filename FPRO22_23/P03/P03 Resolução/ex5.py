n1 = int(input())
n2 = int(input())

result = 0

while((n1 != 0) and (n2 != 0)):
    first = n1 % 10
    result = result * 10 + first
    second = n2 % 10 
    result = result * 10 + second
    n1 = n1 // 10
    n2 = n2 // 10

print(result)
