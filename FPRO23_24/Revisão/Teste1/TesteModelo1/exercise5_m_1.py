def validate_cc(number):
    total = 0
    count = 1

    while number != 0:
        d = number % 10
        if count % 2 == 0:
            d = d * 2
            while d != 0:
                d_2 = d % 10
                total += d_2
                d = d // 10
        else:
            total += d
        count += 1
        number = number // 10


    if (total % 10) == 0:
        return (f"Card number {number} valid")
    else:
        return (f"Card number {number} invalid (checksum {number%10})")
    