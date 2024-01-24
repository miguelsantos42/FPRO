def reversed(n):
    return n[::-1]

def rm_letter_rev(ch,s):
    new_str = ""
    for i in range(0, len(s)):
        if s[i] != ch:
            new_str += s[i]
    return reversed(new_str)

#print(rm_letter_rev("s", "A style guide is about consistency"))
#print(rm_letter_rev(" ", "a nut for a jar of tuna"))
#print(rm_letter_rev("a", "Perfectly good sentence with no need to remove letters"))
#print(rm_letter_rev("l", "Please let me keep my letters!"))
