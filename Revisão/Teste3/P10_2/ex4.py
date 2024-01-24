def union_with(combine, dict1, dict2):
    keys = set(dict1) | set(dict2)
    return {key : combine(dict1[key], dict2[key]) if key in dict1 and key in dict2 else dict1.get(key, dict2.get(key)) for key in keys}

print(sorted(union_with(lambda x,y:x+y, {'a':1, 'b':2}, {'a':3, 'c':4}).items()))
print(sorted(union_with(max, {'a':3, 'b':1, 'c':0}, {'a':1, 'b':3, 'c':2, 'd':5}).items()))
print(sorted(union_with(lambda x,y:x-y, {'a':3, 'b':2, 'c':3}, {'a':2, 'b':1}).items()))
print(sorted(union_with(lambda x,y:x+y, {1:'a', 2:'b', 3:'c'}, {1:'y', 2:'x', 4:'z'}).items()))

