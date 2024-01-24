num = int(input())
aux = num
new_num = 0

while aux != 0:
    d = aux % 10
    new_num = new_num + (d**3)
    aux = aux // 10

if new_num == num:
    print("True")
else:
    print("False")

