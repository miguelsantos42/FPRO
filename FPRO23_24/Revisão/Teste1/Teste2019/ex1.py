num = int(input())
new_num = 0

while num != 0:
    d = num % 10
    new_num = new_num * 10 + d
    num = num // 10

print(new_num)