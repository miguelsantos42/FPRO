def to_fahrenheit(t):
    conversor = map(lambda x : round((x * (9/5) + 32),2),t)
    return list(conversor)

print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]))
print(to_fahrenheit([-5, -2, 0, 2]))
print(to_fahrenheit([]))