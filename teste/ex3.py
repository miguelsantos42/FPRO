def check_romans(alist):
    lista = []
    valid_pairs = ["IV", "IX", "XL", "XC", "CD", "CM"]
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for num in alist:
        valid = True
        for i in range(len(num)):
            if num[i] not in value:
                valid = False
                break
            if i > 0 and value[num[i]] > value[num[i-1]]:
                if num[i-1:i+1] not in valid_pairs:
                    valid = False
                    break
                elif i > 1 and value[num[i]] > value[num[i-2]]:
                    valid = False
                    break
        if valid:
            lista.append(num)

    return lista

print(check_romans(['III', 'XXVI', 'XIX', 'MDCVI']))
print(check_romans(['MCI', 'MIC', 'MMCX', 'MMXC']))
print(check_romans(['CMC', 'CXL', 'CIL', 'DIV', 'DVI']))
print(check_romans(['M111', 'mmcd', 'M C D', 'CCCP']))
