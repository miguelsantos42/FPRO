def discard_middle(s):
    if len(s) <= 3:
        return ""
    new_str = s[0] + s[1] + s[-2] + s[-1]
    return new_str

print(discard_middle('string')) 
print(discard_middle('n')) 
print(discard_middle('abc')) 