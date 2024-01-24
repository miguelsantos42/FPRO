def validate_cc(number):
    number_aux = number
    total = 0
    n = 1
    i = 0 
    k = 0
    while number != 0:
        i = i + (number % 10)
        if (n % 2) == 0:
            k = k + (i * 2)
            while k != 0:
                sub_k = k % 10
                total = total + sub_k
                k = k // 10
        else:
            total = total + i
        number = number // 10
        i = 0
        n = n + 1
        k = 0
    
    if(total % 10 == 0):
        return(f"Card number {number_aux} valid")
    else:
        return(f"Card number {number_aux} invalid (checksum {total%10})")
    
print(validate_cc(4028743156781887))
print(validate_cc(4012888888881882))
print(validate_cc(4712812834781881))
print(validate_cc(4712818234781881))


