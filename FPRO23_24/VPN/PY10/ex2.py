def to_fahrenheit(t):
    return [round((num * (9/5) + 32),2) for num in t]

print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]))
print(to_fahrenheit([-5, -2, 0, 2]))
print(to_fahrenheit([]))