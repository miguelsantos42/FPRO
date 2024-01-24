num = int(input())
for i in range(1,num):
    total = num * i
    print(f'{num} x {i} = {total}')
if(num < 10):
    print(f'{num} ^ 2 = {num**2}')
