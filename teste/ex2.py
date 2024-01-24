def rld(text):
    phrase = ""
    i = 0

    while i < len(text):
        if text[i].isdigit():
            num = ""
            while i < len(text) and text[i].isdigit():
                num += text[i]
                i += 1
            phrase += text[i] * int(num)
        else:
            phrase += text[i]
        i += 1

    return phrase


print(rld("a3bc4b"))
print(rld("10a"))
print(rld("aabbcc"))
print(rld("5*"))
