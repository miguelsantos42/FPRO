def count_chars(a_strings):    
    count_num = 0
    count_char = 0
    count_signs = 0
    for c in a_strings:
        if c.isalpha():
            count_char += 1
        elif c.isnumeric():
            count_num += 1
        else:
            count_signs += 1
    return (count_char, count_num, count_signs)

print(count_chars('Str1nG$'))
print(count_chars('Hello-2019-World'))
