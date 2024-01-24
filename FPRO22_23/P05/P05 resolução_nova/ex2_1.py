

def sinal(string):
    new_str = ""
    pontuacao = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''
    for i in string:
        if i not in pontuacao:
            new_str = new_str + i
    return new_str


def camel_case(phrase):
    new_string = ""
    phrase = phrase.lower()
    i = 0
    pontuacao = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''

    while i < len(phrase):
        if phrase[i] in pontuacao:
            new_string = new_string + phrase[i]
            i = i + 1
            if i < len(phrase):
                new_string = new_string + phrase[i].upper()
                i = i + 1
        else:
            new_string = new_string + phrase[i]
            i = i + 1
    
    final_string = sinal(new_string)

    return final_string

print(camel_case("Testing"))
print(camel_case("One_more_test"))
print(camel_case("NumberOne"))
print(camel_case("What about Now?"))


