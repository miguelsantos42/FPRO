def validate(n):
    is_valide = {
        True : True,
        False : False
    }
    return is_valide[(type(n) is int and 0 <= n <= 100) or (type(n) is float and 0 <= n <= 100)]


print(validate(-10))
print(validate(10.5))
print(validate(-50.2))
print(validate('10'))