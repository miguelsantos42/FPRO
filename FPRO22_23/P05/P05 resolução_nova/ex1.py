def reverse(s):
    return s[::-1]

def rm_letter_rev(ch,s):
    new_string = ""
    for i in s:
        if i == ch:
            i = i.replace(ch, "")
        new_string = new_string + i
    return reverse(new_string)


print(rm_letter_rev("s", "A style guide is about consistency"))
print(rm_letter_rev(" ", "a nut for a jar of tuna"))
print(rm_letter_rev("a", "Perfectly good sentence with no need to remove letters"))
print(rm_letter_rev("l", "Please let me keep my letters!"))
