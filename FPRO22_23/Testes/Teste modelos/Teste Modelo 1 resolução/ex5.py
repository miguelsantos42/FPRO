n = int(input())
total = 0
size_n = 0
sub_num = 0
sub_num_2 = 0

while (n != 0):
    used_n = n % 10
    sub_num = sub_num * 10 + used_n
    n = n // 10

while (sub_num != 0):
    used_sub_num = sub_num % 10
    sub_num_2 = sub_num_2 * 10 + used_sub_num
    sub_num = sub_num // 10
    size_n = size_n + 1


for i in range(0, size_n):
    while (sub_num_2 != 0):
        used_sub_num_2 = sub_num_2 % 10
        total = total + (used_sub_num_2 * 6 ** i)
        sub_num_2 = sub_num_2 // 10
        break

print(total)

