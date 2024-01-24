from functools import reduce

def map_filter_reduce(lst,f1,f2,f3):
    reducao =  list(filter(f1,lst))
    square = list(map(f2, reducao))
    final = reduce(f3, square)
    return final


print(map_filter_reduce([1, 2, 3, 4, 5, 6, 7, 8], lambda i: i % 2 == 0, lambda i: i**2, lambda a, b: a+b))
print(map_filter_reduce([1, 2, 3, 4, 5, 6, 7, 8], lambda i: i < 6, lambda i: 2*i, lambda a, b: a*b))
