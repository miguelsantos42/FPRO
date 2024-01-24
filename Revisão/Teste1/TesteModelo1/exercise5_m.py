def validate_cc(number):
    total = 0
    count = 1
    aux = number

    while aux != 0:
        d = aux % 10
        if count % 2 == 0:
            d = d * 2
            while d != 0:
                d_2 = d % 10
                total += d_2
                d = d // 10
        else:
            total += d
        count += 1
        aux = aux // 10


    if (total % 10) == 0:
        return (f"Card number {number} valid")
    else:
        return (f"Card number {number} invalid (checksum {total%10})")
    


print(validate_cc(4028743156781887))
print(validate_cc(4012888888881882))
print(validate_cc(4712812834781881))
print(validate_cc(4712818234781881))
