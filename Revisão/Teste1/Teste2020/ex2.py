i = int(input())
if i % 2 != 1:
    if i % 7 != 0:
        print(i-2)
    else:
        if i % 11 != 0:
            if i % 3 != 0:
                print(0)
            else:
                if i % 5 != 0:
                    print(5-i)
                else:
                    print(-i)
        else:
            print(3*i+2)
else:
    print(i**2)