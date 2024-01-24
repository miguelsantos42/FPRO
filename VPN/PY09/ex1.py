def to_celsius(t):
    conversor = map(lambda x : round(((x-32)*5)/9,1), t)
    return list(conversor)

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))
print(to_celsius([23.0, 28.4, 32.0, 35.6]))
print([])

