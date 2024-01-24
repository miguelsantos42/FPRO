def inverso(phrase):
    return phrase[::-1]

def rm_letter_rev(ch,s):
    new_phrase = ""
    s = inverso(s)
    for i in range(0, len(s)):
        if s[i] != ch:
            new_phrase = new_phrase + s[i]
    return new_phrase

print(rm_letter_rev("s", "A style guide is about consistency"))
print(rm_letter_rev(" ", "a nut for a jar of tuna"))
print(rm_letter_rev("a", "Perfectly good sentence with no need to remove letters"))
print(rm_letter_rev("l", "Please let me keep my letters!"))
