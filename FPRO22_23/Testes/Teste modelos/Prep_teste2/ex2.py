def remove_sign(s):
    punctuation = "|!#$%&/()=' '_-+*~^?'"
    new_phrase = ""
    for i in s:
        if i not in punctuation:
            new_phrase = new_phrase + i
        else:
            continue
    return new_phrase


def camel_case(phrase):
    new_phrase = ""
    phrase = phrase.lower()
    punctuation = "|!#$%&/()=' '_-+*~^?'"
    i = 0
    while i < len(phrase):
        if phrase[i] in punctuation:
            new_phrase = new_phrase + phrase[i]
            if len(new_phrase) == len(phrase):
                break
            else:
                up = phrase[i+1].upper()
                new_phrase = new_phrase + up
                i = i + 2
        else:
            new_phrase = new_phrase + phrase[i]
            i = i + 1
    
    final_phrase = remove_sign(new_phrase)
    return final_phrase

print(camel_case("Testing"))
print(camel_case("One_more_test"))
print(camel_case("NumberOne"))
print(camel_case("What about Now?"))
