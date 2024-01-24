import string
def remove(phrase):
    final_str = ""
    for i in range(0, len(phrase)):
        if phrase[i].isalpha():
            final_str += phrase[i]
    return final_str

def camel_case(phrase):
    new_str = ""
    final_str = ""
    signals = string.punctuation
    j = 0

    for i in range(0, len(phrase)):
        new_str += phrase[i].lower()

    while j < len(new_str):
        if new_str[j] in signals:
            maisculo = new_str[j+1].upper()
            final_str += new_str[j] + maisculo
            j += 2
        else:
            final_str += new_str[j]
            j += 1

    return remove(final_str)


print(camel_case("Testing"))
print(camel_case("One_more_test"))
print(camel_case("NumberOne"))
print(camel_case("What about Now?"))