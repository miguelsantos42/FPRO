num = int(input())

final_num = 0

while num != 0:
    num_choose = num % 10
    final_num = final_num * 10 + num_choose
    num = num // 10

print(final_num)

