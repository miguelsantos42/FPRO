n = abs(int(input()))
is_looping = True

while n > 10:
    first = n % 10
    n = n // 10
    second = n % 10
    #print(first - second)

    if(first == 9 and second == 0) or (first == 0 and second == 9):
        continue

    if (first - second != 1) and (first - second != -1 ):
        is_looping = False
        break


if(is_looping):
    print("Looping number")
else:
    print("Not a looping number")
