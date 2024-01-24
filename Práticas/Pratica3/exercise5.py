n1 = int(input())
n2 = int(input())

final_num = 0

while n1 != 0:
    final_num = final_num * 10 + (n1 % 10)
    n1 = n1 // 10
    while n2 != 0:
        final_num = final_num * 10 + (n2 % 10)
        n2 = n2 // 10
        break

print(final_num)

