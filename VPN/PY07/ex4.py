def sort(dici):
    return sorted(dici.items(), key = lambda x : x[1])

def sort_by_value(dict):
    return sort(dict)

print(sort_by_value({'Magenta': '#FF00FF', 'Red': '#FF0000', 'White': '#FFFFFF'}))
print(sort_by_value({'Silver': '#C0C0C0', 'Gray': '#808080', 'Tomato': '#FF6347', 'Aqua': '#00FFFF', 'Black': '#000000'}))
print(sort_by_value({'Blue': '#0000FF', 'Red': '#FF0000', 'Green': '#008000', 'Black': '#000000', 'White': '#FFFFFF', 'Gray': '#808080'}))
