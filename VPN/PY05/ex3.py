def discard_middle(s):
    new_string = ""
    if len(s) <= 3:
        return new_string
    new_string += s[0] + s[1] + s[-2] + s[-1]
    return new_string

print(discard_middle('string'))
print(discard_middle('n'))
print(discard_middle('abc'))
