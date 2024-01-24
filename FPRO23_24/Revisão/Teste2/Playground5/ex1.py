import string
def count_chars(a_string):
    count_char = 0
    count_num = 0
    count_symbols = 0
    for i in a_string:
        if i.isalpha():
            count_char += 1
        elif i.isnumeric():
            count_num += 1
        else:
            count_symbols += 1
    return(count_char, count_num, count_symbols)

print(count_chars('Str1nG$'))
print(count_chars('Hello-2019-World'))