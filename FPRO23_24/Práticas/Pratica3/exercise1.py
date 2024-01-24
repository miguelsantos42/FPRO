num = int(input())

for i in range(1,11):
    if i == num:
        print(f"{num} ^ 2 = {num*i}")
        break
    else:
        print(f"{num} x {i} = {num * i}")