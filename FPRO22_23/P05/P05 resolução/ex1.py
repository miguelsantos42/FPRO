def reversed_st(s):
    return s[::-1]

def rm_letter_rev(ch,s):
    final_st = ""
    nova_s = reversed_st(s)
    for i in nova_s:
        if i != ch:
            final_st = final_st + i
        else:
            continue
    return final_st

print(rm_letter_rev("s", "A style guide is about consistency"))
print(rm_letter_rev(" ", "a nut for a jar of tuna"))
print(rm_letter_rev("a", "Perfectly good sentence with no need to remove letters"))
print(rm_letter_rev("l", "Please let me keep my letters!"))
