n = int(input())
a = 0
c = 0

while n != 0:
    if(n%10 >= 8):
        a = - 1
        print("Not a valid number.")
        break
    a += n % 10 * (8**c)
    c += 1
    n //= 10

if a != -1:
    print(a)