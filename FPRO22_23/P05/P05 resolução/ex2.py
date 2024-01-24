import string
def camel_case(phrase):
    maisculas = ("ABCDEFGHIJKLMNOPQRSTUVXYZ")
    minusculas = ("abcdefghijklmnopqrstuvxyz")
    pontuacao = "!#$%&/()=?|"
    now_st = ""
    i = 0

    phrase = phrase.lower()

    while i < len(phrase):
        if phrase[i] in pontuacao:
            if i + 1 < len(phrase):    
                now_st = now_st + phrase[i+1].upper()
            i = i + 2
        else:
            now_st = now_st + phrase[i]
            i = i + 1

    
    return now_st


print(camel_case("Testing"))
print(camel_case("One_more_test"))
print(camel_case("NumberOne"))
print(camel_case("What about Now?"))

