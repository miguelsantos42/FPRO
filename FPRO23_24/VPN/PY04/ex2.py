def count_chars(phrase, letter):
    count = 0
    for i in phrase:
        if i == letter:
            count = count + 1
    if count == 0:
        return -1
    else:   
        return count 

print(count_chars('How much wood would a woodchuck chuck if a woodchuck could chuck wood?', 'w'))
print(count_chars('Eddie edited it', 't'))
print(count_chars('Black back bat', 'd'))
