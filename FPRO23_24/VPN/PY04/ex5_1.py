def get_positions(sentence, word_list):
    string = ""
    lista = sentence.split()
    for i in range(len(lista)):
        for j in range(len(word_list)):
            if lista[i] == word_list[j]:
                string = string + str(j) + ' '
    if string == "0 ":
        return ""
    else:
        return string

print(get_positions('lousy world', ['hello', 'world', 'lousy']))
print(get_positions('lousy lousy', ['hello', 'world', 'lousy']))
print(get_positions('dinosaur goodbye', ['goodbye', 'hello', 'breakfast']))
print(get_positions('breakfast goodbye', ['goodbye', 'hello', 'breakfast']))