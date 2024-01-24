def no_signals(phrase):
    new_str = ""
    signals = "!#$%&/()=/''?,'" "',.-*`_"
    for i in phrase:
        if i not in signals and i != " ":
            new_str += i
    return new_str


def maisculo(phrase):
    new_str = ""
    signals = "!#$%&/()=/'','" "',.-*`_"
    i = 0
    while i < len(phrase):
        if phrase[i] in signals or phrase[i] == " ":
            new_str += phrase[i] + phrase[i+1].upper()
            i = i + 2
        else:
            new_str += phrase[i]
            i += 1
    return new_str


def camel_case(phrase):
    new_str = ""
    final_str = ""
    total_str = ""
    for i in phrase:
        new_str += i.lower()
    final_str += maisculo(new_str)
    total_str += no_signals(final_str)
    return total_str


print(camel_case("Testing"))
print(camel_case("One_more_test"))
print(camel_case("NumberOne"))
print(camel_case("What about Now?"))

