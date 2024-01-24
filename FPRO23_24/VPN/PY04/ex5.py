def get_positions(sentence, word_list):
    string = []  
    for i in sentence.split():
        if i in word_list:
            string.append(str(word_list.index(i)))
    if len(string) == 2:
        return " ".join(string)
    return ""

print(get_positions('lousy world', ['hello', 'world', 'lousy']))
print(get_positions('lousy lousy', ['hello', 'world', 'lousy']))
print(get_positions('dinosaur goodbye', ['goodbye', 'hello', 'breakfast']))
print(get_positions('breakfast goodbye', ['goodbye', 'hello', 'breakfast']))