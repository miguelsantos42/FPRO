def most_frequent(alist):

    dici = {}

    for i in alist:
        if i not in dici:
            dici[i] = 1
        else:
            dici[i] += 1
    
    biggest = None
    max_freq = 0

    for k, v in dici.items():
        if (v > max_freq) or (v == max_freq and k > biggest):
            max_freq = v
            biggest = k

    return biggest

print(most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]))