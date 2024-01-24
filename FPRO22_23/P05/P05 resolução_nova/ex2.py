from string import punctuation

def camel_case(phrase):
    new_string = ""
    phrase = phrase.lower()
    i = 0
    while i < len(phrase)-1:
        if phrase[i] in punctuation:
            new_string = new_string + phrase[i]
            caracter_maisculo = phrase[i+1].upper()
            new_string = new_string + caracter_maisculo
            i = i + 2
        else:
            new_string = new_string + phrase[i]
            i = i + 1
    if new_string == phrase:
        return new_string
    else:
        i = i + 1
        if i == len(phrase) and phrase[i] not in punctuation:
            new_string = new_string + phrase[i]
        else:
            last = phrase.replace(phrase[i], "")
            new_string = new_string + last
        return new_string

print(camel_case("Testing"))
print(camel_case("One_more_test"))
print(camel_case("What about Now?"))
