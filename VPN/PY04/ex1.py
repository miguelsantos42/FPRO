def validate(n):
    if type(n) is not int or n > 100 or n < 0:
        return False
    return True

print(validate(-10))
print(validate(10.5))
print(validate(-50.2))
print(validate('10'))