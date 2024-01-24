def repeated_letter(s):
    for i in range(0, len(s)):
        letter_choose = s[i]
        for j in range(i+1, len(s)):
            if s[j] == letter_choose:
                return s[i]
    return None


print(repeated_letter('tweet'))
print(repeated_letter('like'))
print(repeated_letter('patricia'))
print(repeated_letter('internet'))