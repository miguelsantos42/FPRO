from functools import reduce

def dec2int(alist):
    return reduce(lambda acc, curr : acc*10 + curr, alist)

print(dec2int([1]))
print(dec2int([1,2,3]))
print(dec2int([0,1,2,3]))
print(dec2int([2,0,2,3]))

